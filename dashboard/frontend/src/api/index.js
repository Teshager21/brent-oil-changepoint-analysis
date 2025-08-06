import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';  // <- FIXED

export const fetchPrices = () => axios.get(`${API_BASE_URL}/prices`);
export const fetchChangePoints = () => axios.get(`${API_BASE_URL}/change-points`);
