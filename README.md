# Thomas Hughes — Creative Portfolio

A creative technologist portfolio styled with a dark, cyberpunk/neon aesthetic. Built with standard HTML/CSS/JS.

## Features
- Custom cursor with magnetic effects
- WebGL Noise overlay
- Reveal animations
- Responsive design

## Deployment
This project is configured to deploy automatically to `https://apps.tag-art.co.uk/` via GitHub Actions.

## Setup
To enable deployment:
1. Go to Settings > Secrets > Actions in this repository.
2. Add the following secrets:
   - `SERVER_HOST`: Your server IP or domain.
   - `SERVER_USER`: SSH Username.
   - `SERVER_SSH_KEY`: Your private SSH key.
   - `REMOTE_TARGET`: The path on the server where files should be copied (e.g., `/var/www/html/`).
