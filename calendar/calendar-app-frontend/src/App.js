import React, { useState, useEffect } from 'react';
import CalendarUI from './components/calendarUI';
import { requestNotificationPermission, checkAndShowNotifications } from './notificationUtils';

const App = () => {
  const [events, setEvents] = useState([
    { id: '1', title: 'Meeting', date: '2024-11-10', time: '10:00 AM', description: 'Team meeting' },
    { id: '2', title: 'Conference', date: '2024-11-11', time: '2:00 PM', description: 'Tech conference' }
  ]);

  useEffect(() => {
    requestNotificationPermission();
  }, []);

  // Function to handle saving a new or edited event
  const handleEventSave = (eventData) => {
    setEvents(prevEvents => {
      if (eventData.id) {
        // Update existing event
        return prevEvents.map(event => event.id === eventData.id ? eventData : event);
      } else {
        // Create new event
        return [...prevEvents, eventData];
      }
    });
  };

  // Function to handle deleting an event
  const handleEventDelete = (eventId) => {
    setEvents(prevEvents => prevEvents.filter(event => event.id !== eventId)); 
  };

  useEffect(() => {
    const interval = setInterval(() => checkAndShowNotifications(events), 60000); // every 60 seconds
    return () => clearInterval(interval);
  }, [events]);

  return (
    <div className="App">
      <h1>Event Calendar</h1>
      <CalendarUI
        events={events}
        onEventSave={handleEventSave}
        onEventDelete={handleEventDelete} 
      />
    </div>
  );
};

export default App;
