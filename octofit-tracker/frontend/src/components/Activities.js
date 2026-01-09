import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
      console.log('Fetching activities from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Fetched activities data:', data);
        
        // Handle both paginated and plain array responses
        const activitiesData = data.results || data;
        setActivities(activitiesData);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div>Loading activities...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map(activity => (
          <li key={activity.id} className="list-group-item">
            {activity.user?.name} - {activity.type} - {activity.duration} min - {activity.calories} cal
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;