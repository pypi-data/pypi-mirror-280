import binascii
from genericpath import exists
from playwright.sync_api import sync_playwright
import requests
import base64
import json


class LSPAPI:
    def __init__(self, user, password, key_file, key_file_password) -> None:
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.req_session = requests.session()
        self.user = user
        self.password = password
        self.key_file = key_file
        self.key_file_password = key_file_password

    def start(self):
        """start Initiates the session"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.Login()

    def stop(self):
        """stop Stops the session"""
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def Login(self):
        """Login Logs in to your account

        Raises:
            Exception: Gives Error when Session isn't initialized
            Exception: Gives Error when login credentials are wrong
            Exception: Gives Error when decryption of the keyfile fails
        """

        def encrypt(self, key, text):
            enc = []
            for i in range(len(text)):
                key_c = key[i % len(key)]
                enc_c = chr((ord(text[i]) + ord(key_c)) % 256)
                enc.append(enc_c)
            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        def decrypt(self, key, enc):
            dec = []
            enc = base64.urlsafe_b64decode(enc).decode()
            for i in range(len(enc)):
                key_c = key[i % len(key)]
                dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
                dec.append(dec_c)
            return "".join(dec)

        def get_csrf_token(self):
            # Evaluate JavaScript to get the content of the meta tag with name="csrf-token"
            csrf_token = self.page.evaluate(
                """() => {
                const metaTag = document.querySelector('meta[name="csrf-token"]');
                return metaTag ? metaTag.getAttribute('content') : null;
            }"""
            )
            return csrf_token

        if not exists(self.key_file):
            if not self.page:
                raise Exception("Playwright not started. Call start() before Login().")

            # Open the website
            response = self.page.goto("https://www.leitstellenspiel.de/users/sign_in")

            # Fill out the form
            self.page.fill('input[name="user[email]"]', self.user)
            self.page.fill('input[name="user[password]"]', self.password)

            # Submit the form
            self.page.click('input[name="commit"]')

            # Wait for the form submission to complete
            self.page.wait_for_load_state("networkidle")

            # Check if credentials are invalid
            if '<div class="alert fade in alert-danger ">' in self.page.content():
                raise Exception("Login failed! Check your username and password!")

            # get cookies
            cookies = self.page.context.cookies()
            for i in cookies:
                if i["name"] == "mc_unique_client_id":
                    client_id = i["value"]
                elif i["name"] == "_session_id":
                    session_id = i["value"]

            # Extract CSRF token
            csrf_token = get_csrf_token()

            # generate, encrypt and write keyfile
            filestructure = {
                "mc_unique_client_id": client_id,
                "_session_id": session_id,
                "csrf_token": csrf_token,  # Not needed for now, but good to have laying around.
            }
            fsb64 = base64.urlsafe_b64encode(
                json.dumps(filestructure).encode()
            ).decode()
            fsb_enc = encrypt(self.key_file_password, fsb64)
            with open(self.key_file, "x") as f:
                f.write(fsb_enc)
                f.close()
        else:
            if exists(self.key_file):
                with open(self.key_file, "r") as f:
                    fsb_enc = f.read()
                    f.close()
                try:
                    fsb_dec = base64.urlsafe_b64decode(
                        decrypt(self.key_file_password, fsb_enc)
                    )
                except binascii.Error:
                    raise Exception("Keyfile decryption key invalid!")
                filestructure = json.loads(fsb_dec)

                client_id = filestructure["mc_unique_client_id"]
                session_id = filestructure["_session_id"]
                csrf_token = filestructure["csrf_token"]

            else:
                self.Login()  # Run the function recursively to generate keyfile

        # Set the necessary cookies, headers and auth tokens for requests
        # self.req_session.headers.update(headers)
        self.req_session.cookies.update({"mc_unique_client_id": client_id})
        self.req_session.cookies.update({"_session_id": session_id})

    ###### ACTUAL API FUNCTIONALITY ######

    ## Thanks to Sebastian in this post https://forum.leitstellenspiel.de/index.php?thread/15856-apis/&postID=270314#post270314
    ## for the API routes and docstrings

    def vehicle_states(self):
        """vehicle_states Gibt zurück, wie viel Fahrzeuge sich in welchem Status befinden.

        Raises:
            Exception: Login fail

        Returns:
            json: vehicle states in JSON format
        """
        response = self.req_session.get(
            "https://www.leitstellenspiel.de/api/vehicle_states"
        )
        if "<!DOCTYPE html>" in response.text:
            raise Exception(
                "Could not Login! Are your cookies up to date? Is your password/username correct? Try deleting "
                + self.key_file
            )
        return response.json()

    def user_stats(self):
        """user_stats Gibt Informationen zu dem Spielers zurück (JSON)

        Raises:
            Exception: Login fail

        Returns:
            json: user stats in JSON format
        """
        response = self.req_session.get("https://www.leitstellenspiel.de/api/credits")
        if "<!DOCTYPE html>" in response.text:
            raise Exception(
                "Could not Login! Are your cookies up to date? Is your password/username correct? Try deleting "
                + self.key_file
            )
        return response.json()

    def vehicles(self):
        """Gibt die Fahrzeuge des Spielers zurück

        Raises:
            Exception: Login fail

        Returns:
            json: vehicles of user
        """
        response = self.req_session.get("https://www.leitstellenspiel.de/api/vehicles")
        if "<!DOCTYPE html>" in response.text:
            raise Exception(
                "Could not Login! Are your cookies up to date? Is your password/username correct? Try deleting "
                + self.key_file
            )
        return response.json()

    def buildings(self):
        """Gibt die Gebäude des Spielers zurück 

        Raises:
            Exception: Login fail

        Returns:
            json: Buildings of user
        """
        response = self.req_session.get("https://www.leitstellenspiel.de/api/buildings")
        if "<!DOCTYPE html>" in response.text:
            raise Exception(
                "Could not Login! Are your cookies up to date? Is your password/username correct? Try deleting "
                + self.key_file
            )
        return response.json()


# Just foer testing. Ignore this.
if __name__ == "__main__":
    lsp_api = LSPAPI("myuser", "mypassword", "keyfile.key", "supersecretpassword")
    lsp_api.start()
    try:
        lsp = lsp_api.Login()
        print(lsp_api.vehicle_states())
        print(lsp_api.user_stats())
        print(lsp_api.vehicles())
        print(lsp_api.buildings())

    finally:
        lsp_api.stop()
