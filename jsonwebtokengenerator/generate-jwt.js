const jwt = require('jsonwebtoken');

// Sample payload data
const payload = {
  userId: 123,
  username: 'sampleuser',
  email: 'sampleuser@example.com',
};

// Your JWT secret key
const secret = '7e410c57de9295932d76a36f7e49467d83b98cdfa4288eb237ee92fa66583bfcc29c599cf5d337e24dc768e3a980a4996ca0e7a843a9b1cdcd93ea770cff56b37f4958c1a24bf3bd0e69be75a8c666dd8b3d44152ff0c6417beb7c880b7f72c29767d82b0305b3b8e433bf7d975584918b1bb77254b2f1418b2a5704d790b357'; // Replace with your actual secret key

// Generate JWT
const token = jwt.sign(payload, secret, { expiresIn: '1h' });

console.log('Generated JWT:', token);
