const assert = require('chai').assert;
const {Given, When, Then} = require('cucumber');
const axiosInst = require('../axiosInst').axiosInst;
const uuid = require('uuid');
const config = require('../config');


When('I login as a regular user', async function () {
    let userLogin = {
        email: config.user.email,
        password: config.user.password
    }
    this.res = await axiosInst.post('/accounts/login/', userLogin)
    this.tokens = this.res.data;
    const token = this.tokens['access'];
    this.tokenInterceptor = axiosInst.interceptors.request.use((configAxios) => {
        configAxios.headers.Authorization = `Bearer ${token}`;
        return configAxios;
    });
});