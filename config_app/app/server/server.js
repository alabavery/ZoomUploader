const express = require('express')
const path = require('path');
const fileUtils = require('../files/utils');

const app = express()
const port = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.post('/handler', (req, res) => {
  const { zoomPath, credentials } = req.body;
  Promise.all([
    fileUtils.writeZoomVideosDirectoryPath(zoomPath),
    fileUtils.writeCredentials(credentials),
  ]).then(() => {
    process.exit();
  });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
