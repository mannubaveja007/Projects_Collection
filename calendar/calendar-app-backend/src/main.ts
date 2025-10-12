import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // Allow cross-origin requests from frontend dev server(s)
  app.enableCors();

  const port = process.env.PORT ?? 3000;
  await app.listen(port);
  // Helpful startup log for debugging
  // (shows which process is listening so you don't confuse backend with frontend)
  // Example: "Server listening on http://localhost:3000"
  // Use the PORT env var to run on a different port when needed.
  // e.g. in PowerShell: $env:PORT=3001; npm run start:dev
  // This avoids the "Hello World" backend occupying port 3000 when you want the frontend there.
  // eslint-disable-next-line no-console
  console.log(`Server listening on http://localhost:${port}`);
}
bootstrap();
