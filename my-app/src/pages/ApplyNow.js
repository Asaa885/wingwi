import React, { useState } from 'react';
import axios from 'axios';
import './ApplyNow.css';

const ApplyNow = () => {
    const [formData, setFormData] = useState({
        stName: '',
        email: '',
        combination: '',
        high_school_gpa: '',
        dob: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        const dataToSubmit = {
            ...formData,
            combination: {
                id: 1, // Set appropriate ID based on your logic or use another input field to get it
                combName: formData.combination
            }
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/students/<int:pk>/', dataToSubmit);
            console.log('Response:', response.data);
        } catch (error) {
            console.error('There was an error posting the data!', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className='apply-container'>
            <h3>Apply Now</h3>
            <div className='apply-container label'>
                <label>Name:</label>
                <input 
                    type="text" 
                    name="stName" 
                    value={formData.stName} 
                    onChange={handleChange} 
                    required 
                />
            </div>
            <div>
                <label>Email:</label>
                <input 
                    type="email" 
                    name="email" 
                    value={formData.email} 
                    onChange={handleChange} 
                    required 
                />
            </div>
            <div >
                <label>Combination:</label>
                <input 
                    type="text" 
                    name="combination" 
                    value={formData.combination} 
                    onChange={handleChange} 
                    required 
                />
            </div>
            <div>
                <label>High School GPA:</label>
                <input 
                    type="text" 
                    name="high_school_gpa" 
                    value={formData.high_school_gpa} 
                    onChange={handleChange} 
                    required 
                />
            </div>
            <div>
                <label>Date of Birth:</label>
                <input 
                    type="date" 
                    name="dob" 
                    value={formData.dob} 
                    onChange={handleChange} 
                    required 
                />
                </div>
            </div>
            <button type="submit">Register</button>
        </form>
    );
};

export default ApplyNow;
