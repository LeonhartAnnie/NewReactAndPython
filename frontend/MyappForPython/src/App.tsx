import React, { useEffect, useState } from 'react';

const App: React.FC = () => {
  const [answer, setAnswer] = useState('');

  // Fetch data from Flask API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5001/api/stocks');
        const data = await response.json();
        console.log(data); // 檢查獲取的數據
        setAnswer(data.answer);  // Note the spelling of "anwser"
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Flask & React 結合範例</h1>
      <p>後端返回的數據：{answer}</p>
    </div>
  );
};

export default App