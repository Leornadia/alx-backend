const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    return 'Jobs must be an array';
  }

  jobs.forEach(job => {
    const pushNotificationJob = queue.create('push_notification', job)
      .priority('normal')
      .save((err) => {
        if (err) {
          console.error('Error creating job:', err);
          return false;
        }
        console.log('Notification job created:', job.userId);
        return true;
      });
  });

  return true; // Return true if all jobs are created successfully
}

module.exports = { createPushNotificationsJobs };
