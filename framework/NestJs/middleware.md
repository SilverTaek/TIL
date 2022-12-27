# 미들웨어(Middleware)

- 라우트 핸들러가 클라이언트의 요청을 처리하기 전에 수행되는 컴포넌트
- Nest의 미들웨어는 기본적으로 Express 미들웨어와 동일하게 동작한다.

## 미들웨어 동작

- 어떤 형태의 코드라도 수행할 수 있다.
- 요청과 응답에 변형을 가할 수 있다.(hanging 방지)
- 요청 - 응답 주기를 끝낼 수 있다.
- 여러 개의 미들웨어를 사용한다면 next()로 호출 스택상 다음 미들웨어에게 제어권을 전달한다.

```

import { Injectable } from '@nestjs/common';

@Injectable()
export class LoggerMiddleware {
  use(req, res, next) {
    console.log('Request...');
    next();
  }
}


```

### 미들웨어 적용

```
import { Module } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule {
  configure(consumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes('cats');
  }
}

```

```

import { Module, RequestMethod } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule {
  configure(consumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes({ path: 'cats', method: RequestMethod.GET });
  }
}
```

### MiddlewareConsumer

- 해당 객체를 이용해서 미들웨어를 어디에 적용할 지 관리할 수 있다.

apply(...middleware: (Type<any> | Function)[]): MiddlewareConfigProxy;

```
import { Module } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';
import { CatsController } from './cats/cats.controller';

@Module({
  imports: [CatsModule],
})
export class AppModule {
  configure(consumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes(CatsController);
  }
}
```

### 기능적 미들웨어

```
export function logger(req, res, next) {
  console.log(`Request...`);
  next();
};
```

### 다중 미드웨어

```
consumer.apply(cors(), helmet(), logger).forRoutes(CatsController);

```

### 글로벌 미들웨어

```
const app = await NestFactory.create(AppModule);
app.use(logger);
await app.listen(3000);
```
