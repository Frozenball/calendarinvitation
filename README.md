# Create Calendar Event

A sample Vue.js website using Rails as a backend. View at [calendarinvitation.info](https://calendarinvitation.info).

## Build Setup

``` bash
# Install dependencies
yarn install
cd api && bundle install

# Developing
npm run dev
cd api && ./bin/rails server -e development --binding 127.0.0.1

# Deploy
npm run build
fab deploy
```
