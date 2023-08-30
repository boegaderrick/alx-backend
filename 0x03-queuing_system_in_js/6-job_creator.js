import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
  'phoneNumber': '123456789',
  'message': 'Hello world!',
};

const job = queue.create('push_notification_code', jobData).save((error) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job
  .on('job complete', (result) => {
    console.log('Notification job completed');
  })
  .on('job failed', (error) => {
    console.log('Notification job failed');
  });
