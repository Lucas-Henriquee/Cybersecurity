import express from 'express';
import { OAuth2Client } from 'google-auth-library';
import dotenv from 'dotenv';
import { getUserRole } from './rbac.js';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

app.use(express.static(path.join(__dirname, '../public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.get('/login', (req, res) => {
  const url = client.generateAuthUrl({
    access_type: 'offline',
    scope: ['email', 'profile', 'openid'],
  });
  res.redirect(url);
});

app.get('/callback', async (req, res) => {
  try {
    const { code } = req.query;
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);

    const ticket = await client.verifyIdToken({
      idToken: tokens.id_token,
      audience: process.env.GOOGLE_CLIENT_ID,
    });

    const payload = ticket.getPayload();
    const { name, email, picture } = payload;
    const role = getUserRole(email);
    const profilePicture = picture || 'https://www.gravatar.com/avatar/?d=mp&s=100';

    const roleFile = fs.readFileSync(path.join(__dirname, 'role_view.html'), 'utf-8');
    const roleId = {
      Teacher: 'role-teacher',
      Student: 'role-student',
      Guest: 'role-guest'
    }[role] || 'role-guest';
    const match = roleFile.match(new RegExp(`<div id="${roleId}".*?</div>`, 's'));
    const roleContent = match ? match[0] : '<p>No role content found.</p>';

    res.send(`
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Google OAuth</title>
        <link rel="stylesheet" href="/style.css" />
        <style>
          .role-section {
            margin-top: 40px;
          }
          table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
          }
          th, td {
            padding: 12px;
            border: 1px solid #ccc;
            text-align: left;
          }
          th {
            background-color: #f1f1f1;
          }
          ul {
            text-align: left;
            display: inline-block;
            margin-top: 20px;
          }
          a {
            color: #4285f4;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
          }
          .university-header {
            text-align: center;
            margin-bottom: 40px;
          }
          .university-branding {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
          }
          .ufjf-logo {
            height: 60px;
            object-fit: contain;
          }
          .university-name {
            font-size: 1.8em;
            margin: 0;
            color: #202124;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="university-header">
            <div class="university-branding">
              <img class="ufjf-logo" src="/images/Logo_da_UFJF.jpg" alt="UFJF Logo" />
              <h2 class="university-name">Federal University of Juiz de Fora</h2>
            </div>
          </div>

          <h1>Welcome, ${name}!</h1>
          <img src="${profilePicture}" alt="Profile Picture" style="border-radius: 50%; width: 100px; margin: 20px 0;" />
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Role:</strong> ${role}</p>
          <p>You have been authenticated using Google OAuth 2.0.</p>

          ${roleContent}

          <form action="/" style="margin-top: 40px;">
            <button type="submit">Logout</button>
          </form>
        </div>
      </body>
      </html>
    `);
  } catch (error) {
    console.error('Authentication error:', error);
    res.status(500).send('Authentication failed.');
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});