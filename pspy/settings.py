import configparser
import os


class Settings(object):
    config_filename = '~/.config/pspy/config'

    def __init__(self):
        path_to_config = os.path.expanduser(self.config_filename)
        directory = os.path.dirname(path_to_config)
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            print("Create directory " + directory)
            os.makedirs(directory)
        path_to_config = os.path.abspath(self.config_filename)
        # Check if there is not already a configurtion file
        if not os.path.isfile(path_to_config):
            # Create the configuration file with default settings as it
            # doesn't exist yet
            defaults = {
                'General': {
                    'db_file': '~/.config/pspy/store.db',
                    'thumbnail_directory': '~/.config/pspy/thumbnails'
                }
            }
            self.write(defaults)

    def read(self):
        path_to_config = os.path.expanduser(self.config_filename)
        config = configparser.ConfigParser()
        config.read(path_to_config)
        return config
            # List all contents
            #print("List all contents")
            #for section in config.sections():
            #   print("Section: %s" % section)
            #   for options in config.options(section):
            #       print("x %s:::%s:::%s" % (options,
            #                      config.get(section, options),
            #                      str(type(options))))

            # Print some contents
            #print("\nPrint some contents")
            #print(config.get('other', 'use_anonymous'))  # Just get the value
            #print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?

    def write(self, d):
        # Add content to the file
        config = configparser.ConfigParser()
        for section, options in d.items():
            print("Seccion " + section)
            config.add_section(section)
            for option, value in options.items():
                print(option + " = " + value)
                config.set(section, option, value)
        #Config = ConfigParser.ConfigParser()
        #Config.add_section('mysql')
        #Config.set('mysql', 'host', 'localhost')
        #Config.set('mysql', 'user', 'root')
        #Config.set('mysql', 'passwd', 'my secret password')
        #Config.set('mysql', 'db', 'write-math')
        #Config.add_section('other')
        #Config.set('other',
        #'preprocessing_queue',
        #['preprocessing.scale_and_center',
        #'preprocessing.dot_reduction',
        #'preprocessing.connect_lines'])
        #Config.set('other', 'use_anonymous', True)

        path_to_config = os.path.expanduser(self.config_filename)
        # Create the configuration file as it doesn't exist yet
        with open(path_to_config, 'w+') as config_file:
            config.write(config_file)
        config_file.close()
