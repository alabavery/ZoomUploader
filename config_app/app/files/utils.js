const fs = require('fs');
const { HOME_DIRECTORY_MOUNT, CONFIG_DIR_NAME, ZOOM_DIRECTORY_FILE_NAME } = require('../constants');

const pathExists = async path => fs.existsSync(path);

const CONFIG_DIR_PATH = `${HOME_DIRECTORY_MOUNT}/${CONFIG_DIR_NAME}`;
const configDirExists = async () => pathExists(CONFIG_DIR_PATH);
const makeConfigDir = async () => fs.mkdirSync(CONFIG_DIR_PATH);

const CREDENTIALS_FILE_PATH = `${CONFIG_DIR_PATH}/credentials.json`;
const credentialsFileExists = async () => pathExists(CREDENTIALS_FILE_PATH);
const writeCredentials = async credentials => fs.writeFileSync(CREDENTIALS_FILE_PATH, credentials);

// read the txt file in config that contains the path to the directory where Zoom videos stored
const ZOOM_VIDEOS_DIRECTORY_PATH_FILE_PATH = `${CONFIG_DIR_PATH}/${ZOOM_DIRECTORY_FILE_NAME}`;
const zoomVideosDirectoryPathFileExists = async () => pathExists(ZOOM_VIDEOS_DIRECTORY_PATH_FILE_PATH);
const readZoomVideosDirectoryPath = async () => fs.readFileSync(ZOOM_VIDEOS_DIRECTORY_PATH_FILE_PATH);
const writeZoomVideosDirectoryPath = async path => fs.writeFileSync(ZOOM_VIDEOS_DIRECTORY_PATH_FILE_PATH, path);

module.exports = {
    configDirExists,
    makeConfigDir,
    credentialsFileExists,
    writeCredentials,
    zoomVideosDirectoryPathFileExists,
    readZoomVideosDirectoryPath,
    writeZoomVideosDirectoryPath,
}