import axios from 'axios';

const API_URL = 'http://localhost:3000/events';

export const createEvent = async (eventData) => {
  return axios.post(API_URL, eventData);
};

export const getEvents = async () => {
  return axios.get(API_URL);
};

export const updateEvent = async (id, eventData) => {
  return axios.put(`${API_URL}/${id}`, eventData);
};

export const deleteEvent = async (id) => {
  return axios.delete(`${API_URL}/${id}`);
};
