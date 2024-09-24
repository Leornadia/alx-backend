import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Before each test, create a queue and enter test mode
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  // After each test, clear the queue and exit test mode
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);  // Expect two jobs to be created
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);  // Check first job data
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);  // Check second job data
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');  // Verify job type
  });
});

