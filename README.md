# Sens More Project

Sense More is a smart attendance tracking system for companies and organizations, using indoor tracking. The system allows managers to easily track employee attendance, search and filter employees, communicate via chat, receive company announcements and updates, and view employee statistics such as consumed and remaining vacation days.

## Code Files

The repository contains four main code files:

- `generate_random_data.py`
- `api_reciever.py`
- `main_server_with_RTDB.py`
- `simulate_7_users_devices.py`

### Generate Random Data

In the `generate_random_data.py` file, we generated demo company data and uploaded it to Google Firebase. The company in our demo contains four rooms, two path rooms, an office, a kitchen, and a manager's office. The company also has five departments: HR, IT, Marketing, Sales, and Finance. We generated 10 employees in this company with random departments.

### API Receiver

The `api_receiver.py` file contains a Flask server that receives employee ID and room ID to be stored in Firebase for analysis later.

### Main Server with RTDB

The `main_server_with_RTDB.py` file is similar to the previous file, but with the addition of real-time tracking (tested with only seven employees) for a real-time dashboard.

### Simulate 7 Users Devices

The `simulate_7_users_devices.py` code simulates seven employee devices, with each employee running on a separate thread. The code generates data for each employee in real-time and sends it to the main server for analysis.

## How to Use

To use the project, you will need to clone this repository and install the necessary dependencies. You can then run each code file separately to generate and analyze data.

## Contributing

If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository.

2. Create a new branch:

```git checkout -b feature/your-feature```

3. Make your changes and commit them:

```git commit -m 'Add some feature'```

4. Push to the branch:

```git push origin feature/your-feature```


5. Submit a pull request.

## License

This project is licensed under the `MIT License` - see the [LICENSE](LICENSE) file for details.
