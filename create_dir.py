import argparse
import os
import logging

def config_log(debug=False):
    logger=logging.getLogger()
    level=logging.DEBUG if debug else logging.INFO
    # log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    # level = getattr(logging, log_level, logging.INFO)
    # print(log_level)
    logger.setLevel(level)
    file_handler=logging.FileHandler('audit.log')
    formatter=logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if debug:
        logger.debug('Debug mode enabled')
        print('Debug mode enabled')
    # if level==logging.DEBUG:
    #     logger.debug('Debug mode enabled')
    #     print('Debug mode enabled')
    return logger

def create(logger):
    path = str(input("Enter the path where the folder should be created: "))
    folder_name = str(input("Enter the new folder name: "))
    logger.debug(f"Path: {path}")
    logger.debug(f'Folder name: {folder_name}')
    try:
        full_path = os.path.join(path, folder_name)
        logger.debug(f"Full path: {full_path}")
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            logger.info(f"Folder created: {full_path}")
            print(f"Folder created: {full_path}")
        else:
            logger.error(f"Folder already exists: {full_path}")
            print(f"Folder already exists: {full_path}")
    except FileNotFoundError:
        logger.error(f"Path not found: {path}")
        print(f"Path not found: {path}")
    except PermissionError:
        logger.error(f"Permission denied: {path}")
        print(f"Permission denied: {path}")
    except OSError:
        logger.error(f"Invalid path: {path}")
        print(f"Invalid path: {path}")
        print('Enter a valid path and folder name')
        create(logger)
    except Exception as e:
        logger.error(f"Unknown error occurred: {e}")
        print(f"Unknown error occurred: {e}")

def create_dir():
    parser = argparse.ArgumentParser(description='Create a folder')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    logger=config_log(args.debug)
    # config_log()
    create(logger)

if __name__ == '__main__':
    create_dir()