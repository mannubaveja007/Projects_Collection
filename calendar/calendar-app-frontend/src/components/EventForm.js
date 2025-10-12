import React, { useState, useEffect } from 'react';

const EventForm = ({ event, onSave }) => {
  // Initial state for the form
  const [formData, setFormData] = useState({
    title: '',
    date: '',
    time: '',
    description: '',
  });


  useEffect(() => {
    if (event) {
      setFormData({
        title: event.title || '',
        date: event.date || '',
        time: event.time || '',
        description: event.description || '',
      });
    }
  }, [event]);

  // Handle form input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title || !formData.date || !formData.time) {
      alert('Please fill in all required fields.');
      return;
    }
    onSave(formData);  // Send the form data to the parent for saving
    setFormData({ title: '', date: '', time: '', description: '' });  // Reset form
  };

  return (
    <div className="event-form">
      <h2>{event ? 'Edit Event' : 'Create Event'}</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Event Title:</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="date">Date:</label>
          <input
            type="date"
            id="date"
            name="date"
            value={formData.date}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="time">Time:</label>
          <input
            type="time"
            id="time"
            name="time"
            value={formData.time}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description (Optional):</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
          ></textarea>
        </div>
        <button type="submit">{event ? 'Save Changes' : 'Create Event'}</button>
      </form>
    </div>
  );
};

export default EventForm;
