from flask import Flask, request, render_template
from markupsafe import escape
import re

app = Flask(__name__)
#app.secret_key = 'your_secret_key'  # Needed for flash messages and sessions

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        first_name = escape(request.form.get('first_name', '').strip())
        last_name = escape(request.form.get('last_name', '').strip())
        email = escape(request.form.get('email', '').strip())
        country = escape(request.form.get('country', '').strip())
        message = escape(request.form.get('message', '').strip())
        gender = escape(request.form.get('gender', '').strip())
        subject = request.form.getlist('subject') or ['Others']  # Default to "Others"
        honeypot = request.form.get('honeypot', '').strip()

        # Server-side validation
        errors = {}

        # Validate name
        def validate_field(name, value, pattern, max_length, err_msg):
            if not value:
                errors[name] = f"{err_msg} is required."
            elif not re.match(pattern, value):
                errors[name] = f"{err_msg} contains invalid characters."
            elif len(value) > max_length:
                errors[name] = f"{err_msg} cannot exceed {max_length} characters."

        validate_field('first_name', first_name, r'^[a-zA-Z\s\-]+$', 50, 'First name')
        validate_field('last_name', last_name, r'^[a-zA-Z\s\-]+$', 50, 'Last name')

        # Validate email
        if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors['email'] = "A valid email address is required."
        elif len(email) > 100:
            errors['email'] = "Email cannot exceed 100 characters."

        # Validate country
        if not country:
            errors['country'] = "Country is required."

        # Validate message
        if not message:
            errors['message'] = "Message is required."
        elif len(message) > 500:
            errors['message'] = "Message cannot exceed 500 characters."

        # Validate gender
        if gender not in ['M', 'F']:
            errors['gender'] = "Gender is required."

        # Honeypot anti-spam check
        if honeypot:
            return "Spam detected!", 400
        
        # If there are valitation errors
        if errors:
            # If there are errors, re-render the form with feedback
            return render_template('contact_form.html', errors=errors, form=request.form)

        # If validation passes, show success page
        return render_template('thank_you.html', first_name=first_name, last_name=last_name,
                               email=email, country=country, message=message,
                               gender=gender, subject=", ".join(subject))

    # Render form on GET request
    return render_template('contact_form.html', errors={}, form={})


if __name__ == '__main__':
    app.run(debug=True)
