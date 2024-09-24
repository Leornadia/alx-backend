const kue = require('kue');
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track the job progress (0 out of 100%)
  job.progress(0, 100);

  // Check if the phoneNumber is in the blacklisted array
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job and return the error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update job progress to 50%
  job.progress(50, 100);

  // Simulate sending the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Process jobs in the 'push_notification_code_2' queue, with 2 concurrent jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Handle job events
queue.on('job complete', (id, result) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} completed`);
    job.remove((err) => {
      if (err) throw err;
      console.log(`Removed completed job ${job.id}`);
    });
  });
});

queue.on('job failed', (id, errorMessage) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });
});

queue.on('job progress', (id, progress) => {
  console.log(`Notification job ${id} ${progress}% complete`);
});

