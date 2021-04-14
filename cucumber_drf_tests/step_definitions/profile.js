const assert = require('chai').assert;
const _ = require('lodash');
const {When, Then} = require('cucumber');
const uuid = require('uuid');
const axiosInst = require('../axiosInst').axiosInst;
const config = require('../config');


When('I sent a get request to {string}', async function (path) {
    this.res = await axiosInst.get(`${path}`, config.user);
    this.getUserData = this.res.data;
});

Then('I should receive user data', async function () {
    assert.exists(this.getUserData.username);
    assert.equal(config.user.email, this.getUserData.email);
    assert.equal('http://0.0.0.0:8000/media/users/test_user_image', this.getUserData.image);
});

When('I change my email', async function () {
    let userPatch = {
        email: 'hat.com',
    };
    this.res = await axiosInst.patch('/accounts/profile/', userPatch);
    this.patchedUer = this.res.data;
});

Then('The email should not be changed', async function () {
    assert.equal(this.res.data.email, config.user.email);
});

When('I try to change my username', async function () {
    let userPatch = {
        username: 'test2',
    };
    this.res = await axiosInst.patch('/accounts/profile/', userPatch);
});

Then('I should receive user data with different username', async function () {
    assert.notEqual(this.res.data, config.user.username);
});

When('I send patch request with existing specialty', async function () {
    this.userPatch = {
        specialty: 'Urologist',

    };
    this.res = await axiosInst.patch('/accounts/profile/', this.userPatch);
});

Then('I should be able to get this specialty', async function () {
    assert.equal(this.userPatch.specialty, this.res.data.specialty);
});

When('I send patch request with not existing specialty', async function () {
    let userPatch = {
        specialty: 'test speciality',
    };
    try {
        this.res = await axiosInst.post('/orders/', userPatch);
    } catch (error) {
        this.res = error.response;
    }
});

Then('I should receive error message', function () {
    assert.include(this.res.statusText, 'Not Found');
});

When('I send get request to get all users', async function () {
    this.res = await axiosInst.get('/accounts/all/');
    this.usersList = this.res.data;
});

Then('I should be able to get the list of these users', function () {
    assert.equal(this.usersList.length, 2);
});

When('I send request by id to get foreign user', async function () {
    try {
        this.res = await axiosInst.get('/accounts/profile/2/');
    } catch (error) {
        this.res = error.response;
    }
});