import React from 'react';
import axios from 'axios';

function DeleteAccount() {
  const handleDelete = async () => {
    if (window.confirm('Are you sure you want to delete your account?')) {
      try {
        const token = localStorage.getItem('token');
        await axios.delete(
          '/api/user/delete-account',
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
            data: {
              username: 'YourUsernameHere' // You can dynamically set this based on logged-in user info
            }
          }
        );
        alert('Account deleted successfully');
        localStorage.removeItem('token');
      } catch (error) {
        alert('Error deleting account');
      }
    }
  };

  return (
    <button onClick={handleDelete}>Delete Account</button>
  );
}

export default DeleteAccount;
