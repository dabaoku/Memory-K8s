FROM node:latest

WORKDIR /app

COPY package.json ./

# will execute npm install
RUN npm install

# copies all the file in local directory
COPY . .

# run "npm start" command
CMD ["npm", "start"]