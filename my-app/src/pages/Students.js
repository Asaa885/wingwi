import React, { useEffect, useState } from 'react';
import axios from 'axios';

const StudentList = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    // Fetch data from the API when the component mounts
    axios.get('http://localhost:8000/student/') // URL of Django REST API endpoint
      .then(response => {
        setStudents(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the students!', error);
      });
  }, []);

  return (
    <div>
      <h1>Student List</h1>
        {students.map(student => (
          <p>{student.id} {student.stName} {student.combination.combName}</p>
            
        ))}

    </div>
   );
 };

const CombinationList = () => {
  const [combinations, setCombinations] = useState([]);

  useEffect(() => {
    // Fetch data from the API when the component mounts
    axios.get('http://localhost:8000') // URL of  Django REST API endpoint
      .then(response => {
        setCombinations(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the students!', error);
      });
  }, []);

  return (
    <div>
      <h1>Combination List</h1>
        {combinations.map(combination => (
          <p>{combination.id} {combination.combNameName} {combination.combName}</p>
            
        ))}

    </div>
  );
};

export default CombinationList;
