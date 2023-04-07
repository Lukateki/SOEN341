export interface Applicant {
    applicant_id: Number;
    description: string;
    email: string;
    first_name: string;
    interests: string;
    isApplicant: Boolean;
    isRecruiter: Boolean;
    last_name: string;
    referred_pronouns: string;
    skills: string;
    user_id: Number;
    username: string;
}

export interface JobApplication {
    applicant_id: Number;
    job_id: Number;
}

/* Validation methods for inputs like name, email */
export const isValidName = (name: string) => {
    const nameRegex = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ]+$/;
    return nameRegex.test(name);
}

export const isValidEmail = (email: string) => {
    const emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return emailRegex.test(email);
}