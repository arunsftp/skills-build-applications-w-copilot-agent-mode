import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const codespace = process.env.REACT_APP_CODESPACE_NAME;
        const baseUrl = codespace 
          ? `https://${codespace}-8000.app.github.dev`
          : 'http://localhost:8000';
        const url = `${baseUrl}/api/workouts/`;
        
        console.log('Fetching workouts from:', url);
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsList = data.results || data;
        setWorkouts(workoutsList);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="container mt-4"><div className="alert alert-info">Loading workouts...</div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2>Workout Suggestions</h2>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{workout.title}</h5>
                <h6 className="card-subtitle mb-2 text-muted">
                  <span className={`badge badge-${workout.difficulty === 'beginner' ? 'success' : workout.difficulty === 'intermediate' ? 'warning' : 'danger'}`}>
                    {workout.difficulty.toUpperCase()}
                  </span>
                </h6>
                <p className="card-text">{workout.description}</p>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">
                    <strong>Duration:</strong> {workout.duration_minutes} minutes
                  </li>
                  <li className="list-group-item">
                    <strong>Activity Type:</strong> {workout.activity_type}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
