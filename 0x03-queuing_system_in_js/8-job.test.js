const { createPushNotificationsJobs } = require('./8-job');
const kue = require('kue');
const { expect } = require('chai');

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode = true; // Enter test mode
  });

  afterEach(() => {
    queue.testMode = false; // Exit test mode
    kue.inactive.remove(err => { // Use kue.inactive.remove
      if (err) {
        console.error('Error clearing queue:', err);
      }
    });
  });

  it('should display a error message if jobs is not an array', () => {
    const jobs = 'invalid';
    const errorMessage = createPushNotificationsJobs(jobs);
    expect(errorMessage).to.equal('Jobs must be an array'); 
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { userId: 1, message: 'Hello User 1!' },
      { userId: 2, message: 'Hello User 2!' }
    ];
    const result = createPushNotificationsJobs(jobs, queue);
    expect(result).to.be.true;

    // Validate jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data.userId).to.equal(1);
    expect(queue.testMode.jobs[0].data.message).to.equal('Hello User 1!');
    expect(queue.testMode.jobs[1].data.userId).to.equal(2);
    expect(queue.testMode.jobs[1].data.message).to.equal('Hello User 2!');
  });
});
