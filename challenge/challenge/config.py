import dotenv

def get_configuration():
    #appconfig.update_config()
    environment_file = 'appconfig-env'
    #f = open(environment_file, "w")
    #f.write(appconfig.config)
    #f.close()
    dotenv.read_dotenv(environment_file)