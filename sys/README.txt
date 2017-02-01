initial setup, system startup/shutdown definitions

Setup steps:
    1. install python
    2. install virtualenv
    3. virtualenv venv
        - this will create a new virtual environment named venv
    4. Activate the virtualenv
        - windows - venv\Scripts\activate
        - unix - source venv/bin/activate
    5. install dependencies
        - windows - pip install -r sys\requirements.txt
        - unix - pip install -r sys/requirements.txt
    6. add lib to path
        - Add environment variable to run configuration. i.e."Path=G:\PyCharmProjects\qa-automation-python\lib\win;"
    7. bizprdw-dnet001 uses an invalid security certificate. The certificate is only valid for bus-system-apps.bna.com
        - Add Exception in Firefox to support invalid cert.