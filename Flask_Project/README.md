# Contact Form Flask Project

## **Overview**

This project implements a web-based contact form using the Flask framework in Python. 
The form enables users to contact the technical support team of a company, with features for sanitization, validation, and feedback.

---

## **Features Developed**

### Backend: Python Programming
- Introduction to logical structures.
- Implementation of GET and POST methods.
- Use of Flask's server-side features.

### Sanitization and Validation
- Neutralization of potentially harmful inputs like `<script>` tags.
- Validation of mandatory fields, such as name, email, and gender.
- Validation of email format using regular expressions.

### Templates
- Dynamic rendering of forms and feedback using Jinja templates.
- Proper retention of user input and error messages in case of validation failure.

---

## **Problem Statement**

Hackers Poulette™ aims to provide a secure contact method for users to reach their technical support team. The contact form must:
1. Display a user-friendly interface.
2. Validate and sanitize user input.
3. Prevent spam using honeypot techniques.
4. Provide user feedback on successful submissions or errors.

---

## **Project Structure**

### **Files**
1. **`app.py`**:
   - Core Python script implementing the Flask app.
   - Contains routes and logic for handling GET and POST requests.
   - Implements server-side validation and sanitization.

2. **`contact_form.html`**:
   - HTML template for the contact form.
   - Includes fields for first name, last name, email, gender, country, subject, and message.
   - Displays error messages near the respective fields for user convenience.

3. **`thank_you.html`**:
   - HTML template for the thank-you page displayed after successful form submission.
   - Summarizes the sanitized and validated input provided by the user.

---

## **Performance Criteria**

- **Error Handling**: If a user makes an error, the form is returned with valid inputs preserved and specific error messages displayed.
- **Honeypot Anti-Spam**: An invisible field prevents spam submissions.
- **Validation and Sanitization**:
  - Fields are checked for mandatory input and valid formats.
  - Harmful encodings (e.g., `<script>`) are neutralized.
- **Feedback**: A "Thank You" page is displayed on successful submission with a summary of the data.

---

## **Key Functionalities**

### **Form Fields**
- **Mandatory Fields**: First name, last name, email, country, gender, and message.
- **Optional Fields**: Subject (default is "Others").
- **Validation Rules**:
  - First and last names: Alphabetic characters only, max 50 characters.
  - Email: Valid email format, max 100 characters.
  - Message: Max 500 characters.
  - Gender: Must be either "M" or "F".
  - Honeypot: Must remain empty.

### **Routing**
- **GET Request**: Displays the empty contact form.
- **POST Request**: Processes the form data:
  - Performs validation and sanitization.
  - Renders the thank-you page or the contact form with error messages.

### **Anti-Spam**
- Honeypot field traps bot submissions by requiring the field to remain empty.

---

## **Learning Outcomes**

Upon completing this project, the following concepts were mastered:
1. Differentiation between GET and POST requests.
2. Mitigation of XSS and SSTI vulnerabilities.
3. Basics of deploying Flask applications.
4. Implementation of a secure and user-friendly contact form.

---

## **Conclusion**

This project successfully fulfills the requirements of Hackers Poulette™ by providing a secure, validated, and sanitized contact form. 
Users can conveniently reach out to the technical support team, ensuring a seamless experience. 
The project showcases effective use of Flask, Jinja templates, and robust validation techniques.

---
