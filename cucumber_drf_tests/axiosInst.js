const axios = require('axios');
const config = require('./config');

module.exports = {
    axiosInst: axios.create({
        baseURL: `${config.url}`
    })
};
