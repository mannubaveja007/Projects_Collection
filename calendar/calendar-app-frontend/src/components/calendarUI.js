import React, { useState } from 'react';
import Calendar from 'react-calendar';  // Calendar component
import 'react-calendar/dist/Calendar.css';  // Calendar styles
import EventForm from './EventForm';  // EventForm component to create/edit events

const CalendarUI = ({ events, onEventSave }) => {
  const [selectedDate, setSelectedDate] = useState(null);
  const [showEventForm, setShowEventForm] = useState(false);
  const [selectedEvent, setSelectedEvent] = useState(null);

  // Handle date change on calendar
  const handleDateChange = (date) => {
    setSelectedDate(date);
    setSelectedEvent(null);  
    setShowEventForm(true);  // Show the event form when a date is selected
  };

  // Get events for selected date
  const getEventsForSelectedDate = (date) => {
    return events.filter(event => new Date(event.date).toDateString() === new Date(date).toDateString());
  };

  // Handle saving the event
  const handleSaveEvent = (eventData) => {
    onEventSave(eventData);  
    setShowEventForm(false);  // Close form after saving
  };
 

  return (
    <div className="calendar-ui">
      <h2>Event Calendar</h2>
      <Calendar
        onChange={handleDateChange}  // Update selected date
        value={selectedDate}  // Set the selected date
      />
      <div className="event-list">
        {selectedDate && (
          <>
            <h3>Events for {selectedDate.toDateString()}</h3>
            <ul>
              {getEventsForSelectedDate(selectedDate).map(event => (
                <li key={event.id}>
                  <strong>{event.title}</strong>
                  <p>{event.description}</p>
                  <p>{event.time}</p>
                </li>
              ))}
            </ul>
          </>
        )}
      </div>

      {showEventForm && (
        <EventForm
          event={selectedEvent}  // Pass selected event (if editing)
          onSave={handleSaveEvent}  // Handle save event
        />
      )}
    </div>
  );
};

export default CalendarUI;
