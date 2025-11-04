# Mobile Development

**iOS, Android, React Native, and Flutter development patterns**

## Platform-Specific Development

### iOS (Swift/SwiftUI)

#### Project Structure
```
MyApp/
├── Models/
├── Views/
├── ViewModels/
├── Services/
└── Resources/
```

#### SwiftUI Patterns
```swift
struct ContentView: View {
    @StateObject private var viewModel = ViewModel()

    var body: some View {
        NavigationView {
            List(viewModel.items) { item in
                ItemRow(item: item)
            }
            .navigationTitle("Items")
        }
        .task {
            await viewModel.loadItems()
        }
    }
}
```

### Android (Kotlin/Jetpack Compose)

#### Project Structure
```
app/
├── data/
├── domain/
├── presentation/
│   ├── ui/
│   └── viewmodels/
└── di/
```

#### Jetpack Compose Patterns
```kotlin
@Composable
fun ItemList(viewModel: ItemViewModel = hiltViewModel()) {
    val items by viewModel.items.collectAsState()

    LazyColumn {
        items(items) { item ->
            ItemCard(item = item)
        }
    }
}
```

## Cross-Platform Development

### React Native

#### Component Structure
```typescript
import { StyleSheet, View, Text } from 'react-native'

const MyComponent: React.FC<Props> = ({ title }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
})
```

#### Navigation
```typescript
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'

const Stack = createNativeStackNavigator()

export const App = () => (
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Details" component={DetailsScreen} />
    </Stack.Navigator>
  </NavigationContainer>
)
```

### Flutter

#### Widget Structure
```dart
class MyWidget extends StatelessWidget {
  final String title;

  const MyWidget({Key? key, required this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(16),
      child: Text(
        title,
        style: Theme.of(context).textTheme.headline4,
      ),
    );
  }
}
```

## Mobile Best Practices

### Performance
- Lazy loading
- Image optimization
- List virtualization
- Memory management
- Battery optimization

### Offline Support
- Local data persistence
- Sync strategies
- Conflict resolution
- Cache management

### Security
- Secure storage (Keychain/Keystore)
- Certificate pinning
- Code obfuscation
- Biometric authentication

### App Store Guidelines
- iOS App Store Review Guidelines
- Google Play Store policies
- Privacy policies
- Content ratings

## Testing

### Unit Tests
- Business logic
- ViewModels
- Utility functions

### Widget/Component Tests
- UI components
- User interactions
- State changes

### Integration Tests
- E2E flows
- API integration
- Navigation flows

### Platform Testing
- iOS Simulator
- Android Emulator
- Physical devices
- Cloud device farms (Firebase Test Lab, BrowserStack)

## Deployment

### iOS
- TestFlight beta testing
- App Store Connect
- Provisioning profiles
- Code signing

### Android
- Internal testing track
- Google Play Console
- App signing
- Release management

## Common Patterns

### State Management
- Redux/MobX (React Native)
- Provider/Riverpod (Flutter)
- MVVM (iOS/Android)
- BLoC (Flutter)

### API Integration
- REST APIs
- GraphQL
- WebSockets
- Offline-first sync

### Push Notifications
- Firebase Cloud Messaging
- Apple Push Notification Service
- Local notifications
- Deep linking

