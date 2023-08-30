import { createQueue } from 'kue';

const queue = createQueue();
const blacklist = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  let progress = 0;
  if (blacklist.includes(phoneNumber)) {
    job.progress(progress, 100);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    while (progress < 100) {
      job.progress(progress, 100);
      progress += 50;
    }
    job.complete();
    done();
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
