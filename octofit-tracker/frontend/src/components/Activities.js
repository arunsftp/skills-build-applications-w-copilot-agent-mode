import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const baseUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev`
          : 'http://localhost:8000';
        const url = `${baseUrl}/api/activities/`;
        
        console.log('Fetching activities from:', url);
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Activities data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesList = data.results || data;
        setActivities(activitiesList);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching activities:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="container mt-4"><div className="alert alert-info">Loading activities...</div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <table className="table table-striped table-bordered">
        <thead className="thead-dark">
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Activity Type</th>
            <th>Duration (min)</th>
            <th>Distance (km)</th>
            <th>Calories</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.user_name}</td>
              <td>{activity.activity_type}</td>
              <td>{activity.duration_minutes}</td>
              <td>{activity.distance_km ? activity.distance_km.toFixed(2) : 'N/A'}</td>
              <td>{activity.calories_burned}</td>
              <td>{new Date(activity.date).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
