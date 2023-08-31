import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();
const jobs = [
  {
    phoneNumber: '1234',
    message: 'hello',
  },
  {
    phoneNumber: '6789',
    message: 'world',
  }
];


/*before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});*/


describe('createPushNotificationsJobs', () => {
  it('displays error message if "jobs" is not an array', () => {
    expect(() => createPushNotificationsJobs('test', queue)).to.throw(Error);
    expect(() => createPushNotificationsJobs('test', queue)).to.throw('Jobs is not an array');
  });
  it('succesfully creates jobs', (done) => {
    //for (const jobData of jobs) {
    createPushNotificationsJobs(jobs, queue);
    //}
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    done();
  });
});
