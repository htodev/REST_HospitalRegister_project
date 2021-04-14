const assert = require('chai').assert;
const {Then, When, After} = require('cucumber');
const axiosInst = require('../axiosInst').axiosInst;
const config = require('../config');
const axios = require('axios');


When('I send post request to create new enrollment', async function () {
    this.enrollmentDataPost = {
        patient_name: 'random patient',
        symptoms: 'test symptoms',
        diagnosis: 'test diagnosis',
        room_number: 3

    };
    this.res = await axiosInst.post('/enrollment/', this.enrollmentDataPost);
    this.enrollmentDataCreated = this.res.data;
});

Then('I should receive enrollment data', async function () {
    for (let i = 0; i <= this.enrollmentDataCreated.length; i++) {
        assert.exists(this.billingDataCreated[i]);
    }
});

When('I sent a get request to get my all existing enrolment records', async function () {
    this.res = await axiosInst.get('/enrollment/');
    this.myAllEnrollments = this.res.data;
});
Then('I should be able to get my all enrolments', async function () {
    let ids = [];

    this.myAllEnrollments.forEach(item => {
        return ids.push(item.id);
    });
    assert.notEqual(ids.length, 0)
});

When('I sent a get request to get my own specific enrollment', async function () {
    let id = this.enrollmentDataCreated.id;
    this.res = await axiosInst.get(`/enrollment/${id}/`);
    this.getEnrollment = this.res.data[0];
});

Then('I should be able to get this enrollment', async function () {
    assert.equal(this.enrollmentDataCreated.id, this.getEnrollment.id);
});

When('I sent a patch request to update the existing enrollment', async function () {
    let id = this.enrollmentDataCreated.id;
    let enrollmentPatchData = {
        patient_name: 'random patient2',
        room_number: 7
    };
    this.res = await axiosInst.patch(`/enrollment/${id}/`, enrollmentPatchData);
    this.patchedEnrollment = this.res.data;
});

Then('I should receive enrollment object with different {string}', async function (fields) {
    let fieldsArr = fields.split(',');
    for (let i = 0; i < fieldsArr.length; i++) {
        assert.notEqual(this.patchedEnrollment[fieldsArr[i]], this.enrollmentDataCreated[fieldsArr[i]]);
    }
});





When('I sent a delete request to delete the existing enrollment', async function () {
    let id = this.enrollmentDataCreated.id;
    this.res = await axiosInst.delete(`/enrollment/${id}/`);
});
Then('I should NOT be able to get this enrollment', async function () {
    try {
        await axiosInst.get(`/enrollment/${this.enrollmentDataCreated.id}/`);
    } catch (error) {
        assert.equal(error.response.status, 404);
    }
});