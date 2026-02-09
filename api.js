import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

// Add token to requests if it exists
axios.interceptors.request.use(config => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const loginUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/auth/login`, { username, password });
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('username', response.data.username);
        }
        return response.data;
    } catch (error) {
        console.error("Login error:", error);
        throw error.response ? error.response.data : error;
    }
};

export const registerUser = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/auth/register`, { username, password });
        return response.data;
    } catch (error) {
        console.error("Registration error:", error);
        throw error.response ? error.response.data : error;
    }
};

export const logoutUser = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
};

export const getDashboardStats = async () => {
    // ... existing code ...
    try {
        const response = await axios.get(`${API_URL}/dashboard`);
        return response.data;
    } catch (error) {
        console.error("Error fetching dashboard stats:", error);
        return null;
    }
};

export const getExperiments = async () => {
    try {
        const response = await axios.get(`${API_URL}/experiments`);
        return response.data;
    } catch (error) {
        console.error("Error fetching experiments:", error);
        return [];
    }
};

export const getQuantumResults = async () => {
    try {
        const response = await axios.get(`${API_URL}/quantum`);
        return response.data;
    } catch (error) {
        console.error("Error fetching quantum results:", error);
        return [];
    }
};

export const getPredictions = async () => {
    try {
        const response = await axios.get(`${API_URL}/predictions`);
        return response.data;
    } catch (error) {
        console.error("Error fetching predictions:", error);
        return [];
    }
};

export const getLeaderboard = async () => {
    try {
        const response = await axios.get(`${API_URL}/leaderboard`);
        return response.data;
    } catch (error) {
        console.error("Error fetching leaderboard:", error);
        return [];
    }
};

export const startSimulation = async () => {
    try {
        const response = await axios.post(`${API_URL}/start_simulation`);
        return response.data;
    } catch (error) {
        console.error("Error starting simulation:", error);
        return null;
    }
};
