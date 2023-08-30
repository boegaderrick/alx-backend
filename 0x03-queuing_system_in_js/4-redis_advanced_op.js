import { createClient, print } from 'redis';

const client = createClient()
  .on('ready', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

const schools = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2,
};

for (const [key, value] of Object.entries(schools)) {
  client.HSET('HolbertonSchools', key, value, (error, reply) => {
    if (error) {
      console.log(error);
    } else {
      print(`Reply: ${reply}`);
    }
  });
}

client.HGETALL('HolbertonSchools', (error, value) => {
  if (error) {
    console.log(error);
  } else {
    console.log(value);
  }
});
