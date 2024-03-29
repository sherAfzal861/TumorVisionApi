from make_prediction import predict, process_image
from signin import check_password, get_user_by_email
from signup import add_user
import emailConfirmation
from config import app, mail,create_access_token,request,jsonify,Message

OTPS = {}

# Endpoint for uploading an image and making predictions
@app.route('/predict-tumor', methods=['POST'])
def predict_tumor():
    # Assuming the uploaded image is sent as a file in the request
    uploaded_file = request.files['image']

    # Check if the file is present
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    try:
        img = process_image(uploaded_file)
        predicted_class, confidence = predict(img)

        # Return the result
        return jsonify({'result': {'predicted_class': predicted_class, 'confidence': confidence}}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Signin endpoint
@app.route('/signin', methods=['POST'])
def signin():
    # Retrieve user credentials from the request JSON data
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # Check if the user exists
    user = get_user_by_email(email)
    if not user:
        return jsonify({'error1': 'Invalid credentials'}), 401

    # Check if the provided password is correct
    if not check_password(user.password, password):
        return jsonify({'error2': 'Invalid credentials'}), 401

    # Generate an access token for the signed-in user
    access_token = create_access_token(identity=email)

    return jsonify({'message': 'Successfully signed in', 'access_token': access_token}), 200

@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve user credentials from the request JSON data
    data = request.get_json()
    username = data.get('name')
    email = data.get('email')
    password = data.get('password')
    received_otp=data.get("otp")
    original_otp = OTPS[email]

    if received_otp == original_otp:
        # Check if the user already exists
        existing_user = get_user_by_email(email)
        if existing_user:
            return jsonify({'error': 'User with this email already exists'}), 400

        # Add the new user to the database
        add_user(username, email, password)

        # Generate an access token for the newly signed-up user
        access_token = create_access_token(identity=email)

        return jsonify({'message': 'Successfully signed up', 'access_token': access_token}), 200
    else:
        return jsonify({'error':"otp do not match"}), 401
@app.route('/request_otp', methods=['POST'])
def send_otp():
    otp = emailConfirmation.generate_otp()
    email = request.get_json().get('email')
    OTPS[email] = otp

    msg = Message('Verify Your Email - OTP', sender='sherafzalg666@gmail.com', recipients=[email])
    msg.body = f'Your OTP is: {otp}'
    print(OTPS)
    # mail.send(msg)
    

    return jsonify({'message':'OTP send to '+email+' successfully'})
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
