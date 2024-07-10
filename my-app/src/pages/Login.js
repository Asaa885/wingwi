import React, { useState } from 'react';
import './Login.css'
import axios from 'axios';
import { Link } from 'react-router-dom';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/login/', {
        username,
        password,
      });

      // Handle the tokens as needed, e.g., save to localStorage
      localStorage.setItem('refreshToken', response.data.refresh);
      localStorage.setItem('accessToken', response.data.access);

      // Redirect or update UI as needed
      console.log('Login successful', response.data);
    } catch (error) {
      console.error('Login error', error);
      setError('Invalid credentials');
    }
  };

  return (
    <div className='log-container'>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className='logInput'>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <Link to= "Main/home"><button type="submit">Login</button></Link>
        <p><a href='register'>Create Account</a></p>
      </form>
    </div>
  );
};

export default LoginForm;
