const {Given, Then, When, After} = require('cucumber');
const assert = require('assert');
const axiosInst = require('../axiosInst').axiosInst;
const axios = require('axios');

Given('I have the back-end service up', function () {
    return 0;
});

Then('I should receive response with code {string}', function (expectedCode) {
    const actualStatusCode = this.res.status;
    assert.equal(expectedCode, actualStatusCode);
});


After(function () {
    axiosInst.interceptors.request.eject(this.tokenInterceptor);
});