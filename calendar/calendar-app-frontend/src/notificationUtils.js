// notificationUtils.js
export const requestNotificationPermission = () => {
    if ('Notification' in window && Notification.permission !== 'granted') {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          console.log('Notification permission granted.');
        } else {
          console.log('Notification permission denied.');
        }
      });
    }
  };
  
  export const checkAndShowNotifications = (events) => {
    const currentTime = new Date();
    events.forEach(event => {
      const eventTime = new Date(`${event.date} ${event.time}`);
      
      // Check if the event time is within 5 minutes 
      if (eventTime <= currentTime && eventTime > currentTime - 5 * 60 * 1000) {
        showNotification(event);
      }
    });
  };
  
  const showNotification = (event) => {
    if (Notification.permission === 'granted') {
      const notification = new Notification(`Event: ${event.title}`, {
        body: `Time: ${event.time} - ${event.description}`,
        icon: '/path/to/icon.png',
      });
  
      // Dismiss notification after 5 seconds
      setTimeout(() => notification.close(), 5000);
  
      // Add snooze action 
      notification.onclick = () => {
        notification.close();
        setTimeout(() => showNotification(event), 5 * 60 * 1000);
      };
    }
  };
  