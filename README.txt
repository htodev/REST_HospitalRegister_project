                         ENROLL SYSTEM

The purpose of this design is to create Django Rest project.
That system will help hospitals monitor admitted patients and
their doctors. It will also contain basic information
about the condition of the patients. Тhe requirements are as
follows:

    * Each doctor must have  an user.
    * Each doctor  must list himself at define endpoint,
    which will be accessible to everyone.
    * Each doctor must keep a record of the patients admitted to it
    at special endpoint for that.
    * This record is accessible only for the doctors.
    * The doctor can delete or update the registry, but only for patients,
    related to it.
    * Only doctors can filter registry by doctors name.
    * There must be a list with names of all hospitalized patients visible to
    everyone.
    * Only admin and doctors (owners of the profile) can edin the profile.

