// In src/index.js
const express = require("express");
const multer = require("multer");

const app = express();
const storage = multer.diskStorage({
  destination: "uploads/",
  filename: function (req, file, cb) {
    cb(null, file.fieldname + "-" + Date.now() + ".JPEG"); // Change the file extension to .jpg
  },
});
const fs = require("fs");

const upload = multer({ storage: storage });
const PORT = process.env.PORT || 3000;

// For testing purposes
app.get("/", (req, res) => {
  res.send("<h2>It's Working!</h2>");
});

app.get("/gy", (req, res) => {
  res.send("<h2>It's Working!</h2>");
      console.log("requested");
});
// Route to handle image uploads
app.post("/upload", upload.single("image"), (req, res) => {

    console.log("Image_requested");

  if (!req.file) {
    res.status(400).send("No image file received");
  } else {
    // Handle the received image here
    const imageFilePath = req.file.buffer;
    // Use the imageFilePath to perform any required processing

    // Example response
    res.send(`Image uploaded and received at: ${imageFilePath}`);
  }
});

app.listen(PORT, () => {
  console.log(`API is listening on port ${PORT}`);
});
//curl -X POST -F "image=@C:/Users/Anonymous Guy/Downloads/image.jpg" http://localhost:3000/upload
////
/*const express = require('express');
const app = express();
const fs = require('fs');

app.post('/upload', (req, res) => {
  const boundary = req.headers['content-type'].split('boundary=')[1];
  let imageBuffer = null;

  req.on('data', (chunk) => {
    if (imageBuffer === null) {
      const startIndex = chunk.indexOf(boundary) + boundary.length + 2;
      const endIndex = chunk.indexOf(boundary, startIndex) - 2;
      imageBuffer = chunk.slice(startIndex, endIndex);
    } else {
      imageBuffer = Buffer.concat([imageBuffer, chunk]);
    }
  });

  req.on('end', () => {
    // Save the image buffer as a JPEG file
    fs.writeFile('received_image.jpg', imageBuffer, (err) => {
      if (err) {
        console.error(err);
        res.sendStatus(500);
      } else {
        console.log('Image saved as received_image.jpg');
        res.sendStatus(200);
      }
    });
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
*/

