FROM node:slim
RUN mkdir app && cd app
COPY . .
# Install puppeteer so it's available in the container.
RUN npm i
CMD npm start