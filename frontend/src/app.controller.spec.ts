import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [AppService],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  describe('root', () => {
    it('should return "Welcome to Intern App Frontend!"', () => {
      expect(appController.getHello()).toBe('Welcome to Intern App Frontend!');
    });
  });

  describe('health', () => {
    it('should return health status', () => {
      const result = appController.healthCheck();
      expect(result).toHaveProperty('status', 'healthy');
      expect(result).toHaveProperty('timestamp');
    });
  });
});
