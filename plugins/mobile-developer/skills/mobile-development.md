# Mobile Development Skill

Comprehensive iOS and Android native mobile development patterns, architectures, frameworks, and best practices for building production-ready mobile applications.

## Overview

This skill covers iOS development (Swift, SwiftUI, UIKit, Combine), Android development (Kotlin, Jetpack Compose, Coroutines), mobile architecture patterns (MVVM, Clean Architecture), offline-first design, push notifications, deep linking, in-app purchases, and mobile security.

## iOS Development

### Swift Language Fundamentals

**Swift Best Practices**:
- Use value types (struct) over reference types (class) when possible
- Leverage protocol-oriented programming
- Use optionals safely (guard let, if let, optional chaining)
- Prefer immutability (let over var)
- Use type inference but be explicit when it improves clarity

**Modern Swift Features**:
```swift
// Async/Await (iOS 15+)
func fetchUser(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// Swift Concurrency with actors
actor UserCache {
    private var cache: [String: User] = [:]

    func getUser(id: String) -> User? {
        cache[id]
    }

    func setUser(_ user: User) {
        cache[user.id] = user
    }
}

// Result builders (SwiftUI)
@ViewBuilder
func makeView() -> some View {
    if isLoggedIn {
        HomeView()
    } else {
        LoginView()
    }
}
```

**Memory Management**:
```swift
// Avoid retain cycles with weak/unowned
class ViewController: UIViewController {
    var onComplete: (() -> Void)?

    func setupCallback() {
        viewModel.onUpdate = { [weak self] in
            self?.updateUI()
        }
    }
}

// Proper closure capture
class DataLoader {
    func loadData(completion: @escaping (Result<Data, Error>) -> Void) {
        URLSession.shared.dataTask(with: url) { [weak self] data, response, error in
            guard let self = self else { return }
            // Process data
        }.resume()
    }
}
```

### SwiftUI (Modern Declarative UI)

**SwiftUI Fundamentals**:
```swift
// State management
struct ContentView: View {
    @State private var count = 0
    @StateObject private var viewModel = ContentViewModel()
    @EnvironmentObject var appState: AppState

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}

// View composition
struct ProfileView: View {
    let user: User

    var body: some View {
        VStack(spacing: 16) {
            ProfileHeaderView(user: user)
            ProfileStatsView(stats: user.stats)
            ProfileActionsView(userId: user.id)
        }
    }
}

// Custom modifiers
struct PrimaryButtonStyle: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(8)
    }
}

extension View {
    func primaryButtonStyle() -> some View {
        modifier(PrimaryButtonStyle())
    }
}
```

**SwiftUI Navigation (iOS 16+)**:
```swift
// Navigation stack
struct AppView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            ListView()
                .navigationDestination(for: User.self) { user in
                    UserDetailView(user: user)
                }
                .navigationDestination(for: Post.self) { post in
                    PostDetailView(post: post)
                }
        }
    }
}

// Sheet presentation
struct ParentView: View {
    @State private var showingSheet = false

    var body: some View {
        Button("Show Sheet") {
            showingSheet = true
        }
        .sheet(isPresented: $showingSheet) {
            SheetView()
        }
    }
}
```

**SwiftUI Lists & Data**:
```swift
// Efficient lists
struct UserListView: View {
    @StateObject private var viewModel = UserListViewModel()

    var body: some View {
        List {
            ForEach(viewModel.users) { user in
                UserRowView(user: user)
                    .onAppear {
                        // Pagination
                        if user == viewModel.users.last {
                            viewModel.loadMore()
                        }
                    }
            }
            .onDelete(perform: viewModel.deleteUsers)
        }
        .refreshable {
            await viewModel.refresh()
        }
        .searchable(text: $viewModel.searchText)
    }
}
```

### UIKit (Traditional Imperative UI)

**UIKit Fundamentals**:
```swift
// View controller lifecycle
class HomeViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        setupConstraints()
        bindViewModel()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        viewModel.fetchData()
    }

    private func setupUI() {
        view.backgroundColor = .systemBackground
        view.addSubview(tableView)
        view.addSubview(loadingIndicator)
    }

    private func setupConstraints() {
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
        ])
    }
}

// Custom views
class CustomButton: UIButton {
    override init(frame: CGRect) {
        super.init(frame: frame)
        configure()
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
        configure()
    }

    private func configure() {
        backgroundColor = .systemBlue
        setTitleColor(.white, for: .normal)
        layer.cornerRadius = 8
        titleLabel?.font = .systemFont(ofSize: 16, weight: .semibold)
    }
}
```

**Auto Layout**:
```swift
// Programmatic constraints
let label = UILabel()
label.translatesAutoresizingMaskIntoConstraints = false
view.addSubview(label)

NSLayoutConstraint.activate([
    label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
    label.widthAnchor.constraint(lessThanOrEqualTo: view.widthAnchor, constant: -32)
])

// Stack views
let stackView = UIStackView(arrangedSubviews: [titleLabel, subtitleLabel, button])
stackView.axis = .vertical
stackView.spacing = 12
stackView.alignment = .fill
stackView.distribution = .equalSpacing
```

**UITableView & UICollectionView**:
```swift
// Modern UITableView
class UsersViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    private let tableView = UITableView()
    private var users: [User] = []

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.register(UserCell.self, forCellReuseIdentifier: "UserCell")
        tableView.dataSource = self
        tableView.delegate = self
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return users.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "UserCell", for: indexPath) as! UserCell
        cell.configure(with: users[indexPath.row])
        return cell
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let user = users[indexPath.row]
        let detailVC = UserDetailViewController(user: user)
        navigationController?.pushViewController(detailVC, animated: true)
    }
}

// Diffable data source (iOS 13+)
class ModernTableViewController: UIViewController {
    typealias DataSource = UITableViewDiffableDataSource<Section, User>
    typealias Snapshot = NSDiffableDataSourceSnapshot<Section, User>

    private var dataSource: DataSource!

    private func configureDataSource() {
        dataSource = DataSource(tableView: tableView) { tableView, indexPath, user in
            let cell = tableView.dequeueReusableCell(withIdentifier: "UserCell", for: indexPath) as! UserCell
            cell.configure(with: user)
            return cell
        }
    }

    private func applySnapshot(users: [User], animatingDifferences: Bool = true) {
        var snapshot = Snapshot()
        snapshot.appendSections([.main])
        snapshot.appendItems(users)
        dataSource.apply(snapshot, animatingDifferences: animatingDifferences)
    }
}
```

### Combine (Reactive Programming)

**Combine Fundamentals**:
```swift
import Combine

// Publishers and subscribers
class SearchViewModel {
    @Published var searchText = ""
    private var cancellables = Set<AnyCancellable>()

    init() {
        $searchText
            .debounce(for: .milliseconds(300), scheduler: DispatchQueue.main)
            .removeDuplicates()
            .filter { !$0.isEmpty }
            .flatMap { text in
                self.searchAPI(query: text)
                    .catch { _ in Just([]) }
            }
            .receive(on: DispatchQueue.main)
            .sink { [weak self] results in
                self?.updateResults(results)
            }
            .store(in: &cancellables)
    }

    private func searchAPI(query: String) -> AnyPublisher<[Result], Error> {
        URLSession.shared.dataTaskPublisher(for: url)
            .map(\.data)
            .decode(type: [Result].self, decoder: JSONDecoder())
            .eraseToAnyPublisher()
    }
}

// Combining publishers
let publisher1 = fetchUser()
let publisher2 = fetchPosts()

Publishers.Zip(publisher1, publisher2)
    .sink(receiveCompletion: { completion in
        // Handle completion
    }, receiveValue: { user, posts in
        // Use both values
    })
    .store(in: &cancellables)
```

### Core Data (Local Database)

**Core Data Stack**:
```swift
// Persistent container
class CoreDataStack {
    static let shared = CoreDataStack()

    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "MyApp")
        container.loadPersistentStores { description, error in
            if let error = error {
                fatalError("Unable to load persistent stores: \(error)")
            }
        }
        return container
    }()

    var context: NSManagedObjectContext {
        persistentContainer.viewContext
    }

    func saveContext() {
        let context = persistentContainer.viewContext
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                let nserror = error as NSError
                fatalError("Unresolved error \(nserror), \(nserror.userInfo)")
            }
        }
    }
}

// CRUD operations
class UserRepository {
    private let context = CoreDataStack.shared.context

    func createUser(name: String, email: String) -> User {
        let user = User(context: context)
        user.id = UUID()
        user.name = name
        user.email = email
        user.createdAt = Date()
        CoreDataStack.shared.saveContext()
        return user
    }

    func fetchUsers() -> [User] {
        let request = User.fetchRequest()
        request.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]
        do {
            return try context.fetch(request)
        } catch {
            print("Error fetching users: \(error)")
            return []
        }
    }

    func deleteUser(_ user: User) {
        context.delete(user)
        CoreDataStack.shared.saveContext()
    }
}
```

## Android Development

### Kotlin Language Fundamentals

**Kotlin Best Practices**:
```kotlin
// Null safety
fun processUser(user: User?) {
    user?.let { u ->
        println("Processing user: ${u.name}")
        saveUser(u)
    } ?: run {
        println("User is null")
    }
}

// Extension functions
fun String.isValidEmail(): Boolean {
    return android.util.Patterns.EMAIL_ADDRESS.matcher(this).matches()
}

// Data classes
data class User(
    val id: String,
    val name: String,
    val email: String,
    val age: Int? = null
) {
    fun isAdult() = age?.let { it >= 18 } ?: false
}

// Sealed classes for state
sealed class UiState<out T> {
    object Loading : UiState<Nothing>()
    data class Success<T>(val data: T) : UiState<T>()
    data class Error(val message: String) : UiState<Nothing>()
}

// When expressions
fun handleState(state: UiState<User>) {
    when (state) {
        is UiState.Loading -> showLoading()
        is UiState.Success -> showUser(state.data)
        is UiState.Error -> showError(state.message)
    }
}
```

**Coroutines (Async Programming)**:
```kotlin
import kotlinx.coroutines.*

// Basic coroutines
class UserViewModel : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()

    fun loadUsers() {
        viewModelScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    repository.fetchUsers()
                }
                _users.value = result
            } catch (e: Exception) {
                // Handle error
            }
        }
    }
}

// Parallel execution
suspend fun loadUserProfile(userId: String): UserProfile {
    return coroutineScope {
        val userDeferred = async { fetchUser(userId) }
        val postsDeferred = async { fetchUserPosts(userId) }
        val followersDeferred = async { fetchFollowers(userId) }

        UserProfile(
            user = userDeferred.await(),
            posts = postsDeferred.await(),
            followers = followersDeferred.await()
        )
    }
}

// Flow for reactive streams
class UserRepository {
    fun observeUsers(): Flow<List<User>> = flow {
        while (true) {
            val users = fetchUsers()
            emit(users)
            delay(30000) // Refresh every 30 seconds
        }
    }

    fun searchUsers(query: String): Flow<List<User>> =
        userDao.searchUsers(query)
            .map { entities -> entities.map { it.toModel() } }
            .flowOn(Dispatchers.IO)
}
```

### Jetpack Compose (Modern Declarative UI)

**Compose Fundamentals**:
```kotlin
// Basic composables
@Composable
fun UserProfile(user: User, modifier: Modifier = Modifier) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .padding(16.dp)
    ) {
        Text(
            text = user.name,
            style = MaterialTheme.typography.headlineMedium
        )
        Spacer(modifier = Modifier.height(8.dp))
        Text(
            text = user.email,
            style = MaterialTheme.typography.bodyMedium
        )
    }
}

// State management
@Composable
fun CounterScreen() {
    var count by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text("Count: $count")
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}

// ViewModel integration
@Composable
fun UserListScreen(viewModel: UserViewModel = viewModel()) {
    val users by viewModel.users.collectAsState()
    val isLoading by viewModel.isLoading.collectAsState()

    LaunchedEffect(Unit) {
        viewModel.loadUsers()
    }

    Box(modifier = Modifier.fillMaxSize()) {
        if (isLoading) {
            CircularProgressIndicator(modifier = Modifier.align(Alignment.Center))
        } else {
            LazyColumn {
                items(users) { user ->
                    UserListItem(user = user)
                }
            }
        }
    }
}
```

**Compose Navigation**:
```kotlin
// Navigation setup
@Composable
fun AppNavigation() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            HomeScreen(onNavigateToProfile = { userId ->
                navController.navigate("profile/$userId")
            })
        }
        composable(
            route = "profile/{userId}",
            arguments = listOf(navArgument("userId") { type = NavType.StringType })
        ) { backStackEntry ->
            val userId = backStackEntry.arguments?.getString("userId")
            ProfileScreen(userId = userId!!)
        }
    }
}
```

**Material Design 3 (Material You)**:
```kotlin
// Theme setup
@Composable
fun MyAppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) {
        darkColorScheme()
    } else {
        lightColorScheme()
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}

// Material components
@Composable
fun UserCard(user: User, onClick: () -> Unit) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
            .clickable(onClick = onClick),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            AsyncImage(
                model = user.avatarUrl,
                contentDescription = "User avatar",
                modifier = Modifier
                    .size(48.dp)
                    .clip(CircleShape)
            )
            Spacer(modifier = Modifier.width(16.dp))
            Column {
                Text(
                    text = user.name,
                    style = MaterialTheme.typography.titleMedium
                )
                Text(
                    text = user.email,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
        }
    }
}
```

### Android Jetpack Components

**ViewModel**:
```kotlin
class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _uiState = MutableStateFlow<UiState<User>>(UiState.Loading)
    val uiState: StateFlow<UiState<User>> = _uiState.asStateFlow()

    fun loadUser(userId: String) {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val user = repository.getUser(userId)
                _uiState.value = UiState.Success(user)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

// ViewModel factory with dependency injection
class UserViewModelFactory(
    private val repository: UserRepository
) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(UserViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return UserViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
```

**Room Database**:
```kotlin
// Entity
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    @ColumnInfo(name = "name") val name: String,
    @ColumnInfo(name = "email") val email: String,
    @ColumnInfo(name = "created_at") val createdAt: Long
)

// DAO
@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY name ASC")
    fun getAllUsers(): Flow<List<UserEntity>>

    @Query("SELECT * FROM users WHERE id = :userId")
    suspend fun getUserById(userId: String): UserEntity?

    @Query("SELECT * FROM users WHERE name LIKE '%' || :query || '%'")
    fun searchUsers(query: String): Flow<List<UserEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUser(user: UserEntity)

    @Delete
    suspend fun deleteUser(user: UserEntity)

    @Update
    suspend fun updateUser(user: UserEntity)
}

// Database
@Database(entities = [UserEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao

    companion object {
        @Volatile
        private var INSTANCE: AppDatabase? = null

        fun getDatabase(context: Context): AppDatabase {
            return INSTANCE ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "app_database"
                )
                    .fallbackToDestructiveMigration()
                    .build()
                INSTANCE = instance
                instance
            }
        }
    }
}
```

**WorkManager (Background Tasks)**:
```kotlin
class SyncWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        return try {
            syncData()
            Result.success()
        } catch (e: Exception) {
            if (runAttemptCount < 3) {
                Result.retry()
            } else {
                Result.failure()
            }
        }
    }

    private suspend fun syncData() {
        // Perform sync
    }
}

// Schedule work
fun scheduleSyncWork(context: Context) {
    val constraints = Constraints.Builder()
        .setRequiredNetworkType(NetworkType.CONNECTED)
        .setRequiresBatteryNotLow(true)
        .build()

    val syncRequest = PeriodicWorkRequestBuilder<SyncWorker>(
        15, TimeUnit.MINUTES
    )
        .setConstraints(constraints)
        .build()

    WorkManager.getInstance(context)
        .enqueueUniquePeriodicWork(
            "sync_work",
            ExistingPeriodicWorkPolicy.KEEP,
            syncRequest
        )
}
```

## Mobile Architecture Patterns

### MVVM (Model-View-ViewModel)

**iOS MVVM with Combine**:
```swift
// Model
struct User: Codable, Identifiable {
    let id: String
    let name: String
    let email: String
}

// ViewModel
class UserListViewModel: ObservableObject {
    @Published var users: [User] = []
    @Published var isLoading = false
    @Published var errorMessage: String?

    private let repository: UserRepository
    private var cancellables = Set<AnyCancellable>()

    init(repository: UserRepository = UserRepository()) {
        self.repository = repository
    }

    func loadUsers() {
        isLoading = true

        repository.fetchUsers()
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { [weak self] completion in
                self?.isLoading = false
                if case .failure(let error) = completion {
                    self?.errorMessage = error.localizedDescription
                }
            }, receiveValue: { [weak self] users in
                self?.users = users
            })
            .store(in: &cancellables)
    }
}

// View (SwiftUI)
struct UserListView: View {
    @StateObject private var viewModel = UserListViewModel()

    var body: some View {
        NavigationView {
            List(viewModel.users) { user in
                UserRowView(user: user)
            }
            .navigationTitle("Users")
            .onAppear {
                viewModel.loadUsers()
            }
        }
    }
}
```

**Android MVVM with Compose**:
```kotlin
// Model
data class User(
    val id: String,
    val name: String,
    val email: String
)

// ViewModel
class UserListViewModel(
    private val repository: UserRepository
) : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()

    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()

    private val _error = MutableStateFlow<String?>(null)
    val error: StateFlow<String?> = _error.asStateFlow()

    fun loadUsers() {
        viewModelScope.launch {
            _isLoading.value = true
            try {
                val result = repository.fetchUsers()
                _users.value = result
                _error.value = null
            } catch (e: Exception) {
                _error.value = e.message
            } finally {
                _isLoading.value = false
            }
        }
    }
}

// View (Compose)
@Composable
fun UserListScreen(viewModel: UserListViewModel = viewModel()) {
    val users by viewModel.users.collectAsState()
    val isLoading by viewModel.isLoading.collectAsState()

    LaunchedEffect(Unit) {
        viewModel.loadUsers()
    }

    if (isLoading) {
        CircularProgressIndicator()
    } else {
        LazyColumn {
            items(users) { user ->
                UserListItem(user = user)
            }
        }
    }
}
```

### Clean Architecture

**Layer Structure**:
```
Presentation Layer (UI + ViewModels)
    ↓
Domain Layer (Use Cases + Entities)
    ↓
Data Layer (Repositories + Data Sources)
```

**iOS Clean Architecture**:
```swift
// Domain Layer - Entities
struct User {
    let id: String
    let name: String
    let email: String
}

// Domain Layer - Use Case
protocol FetchUsersUseCase {
    func execute() -> AnyPublisher<[User], Error>
}

class FetchUsersUseCaseImpl: FetchUsersUseCase {
    private let repository: UserRepository

    init(repository: UserRepository) {
        self.repository = repository
    }

    func execute() -> AnyPublisher<[User], Error> {
        repository.getUsers()
    }
}

// Data Layer - Repository Protocol
protocol UserRepository {
    func getUsers() -> AnyPublisher<[User], Error>
}

// Data Layer - Repository Implementation
class UserRepositoryImpl: UserRepository {
    private let remoteDataSource: RemoteUserDataSource
    private let localDataSource: LocalUserDataSource

    func getUsers() -> AnyPublisher<[User], Error> {
        localDataSource.getCachedUsers()
            .catch { _ in
                self.remoteDataSource.fetchUsers()
                    .flatMap { users in
                        self.localDataSource.cacheUsers(users)
                            .map { users }
                    }
            }
            .eraseToAnyPublisher()
    }
}

// Presentation Layer
class UserListViewModel: ObservableObject {
    @Published var users: [User] = []
    private let fetchUsersUseCase: FetchUsersUseCase

    func loadUsers() {
        fetchUsersUseCase.execute()
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { _ in },
                  receiveValue: { [weak self] in self?.users = $0 })
            .store(in: &cancellables)
    }
}
```

**Android Clean Architecture**:
```kotlin
// Domain Layer - Entity
data class User(
    val id: String,
    val name: String,
    val email: String
)

// Domain Layer - Use Case
interface FetchUsersUseCase {
    suspend operator fun invoke(): Result<List<User>>
}

class FetchUsersUseCaseImpl(
    private val repository: UserRepository
) : FetchUsersUseCase {
    override suspend fun invoke(): Result<List<User>> {
        return repository.getUsers()
    }
}

// Data Layer - Repository
interface UserRepository {
    suspend fun getUsers(): Result<List<User>>
}

class UserRepositoryImpl(
    private val remoteDataSource: RemoteUserDataSource,
    private val localDataSource: LocalUserDataSource
) : UserRepository {
    override suspend fun getUsers(): Result<List<User>> {
        return try {
            // Try cache first
            val cached = localDataSource.getCachedUsers()
            if (cached.isNotEmpty()) {
                Result.success(cached)
            } else {
                // Fetch from network
                val users = remoteDataSource.fetchUsers()
                localDataSource.cacheUsers(users)
                Result.success(users)
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}

// Presentation Layer
class UserListViewModel(
    private val fetchUsersUseCase: FetchUsersUseCase
) : ViewModel() {
    private val _users = MutableStateFlow<List<User>>(emptyList())
    val users: StateFlow<List<User>> = _users.asStateFlow()

    fun loadUsers() {
        viewModelScope.launch {
            fetchUsersUseCase().fold(
                onSuccess = { _users.value = it },
                onFailure = { /* Handle error */ }
            )
        }
    }
}
```

## Offline-First Architecture

### iOS Offline-First with Core Data

```swift
class OfflineFirstRepository {
    private let coreDataStack: CoreDataStack
    private let apiClient: APIClient

    func fetchPosts() -> AnyPublisher<[Post], Error> {
        // 1. Return cached data immediately
        let localPosts = fetchLocalPosts()

        // 2. Fetch from network and update cache
        return apiClient.fetchPosts()
            .handleEvents(receiveOutput: { [weak self] posts in
                self?.cachePosts(posts)
            })
            .catch { _ in
                // If network fails, return cached data
                Just(localPosts)
            }
            .eraseToAnyPublisher()
    }

    func createPost(_ post: Post) -> AnyPublisher<Post, Error> {
        // 1. Save locally immediately
        let savedPost = savePostLocally(post, synced: false)

        // 2. Try to sync with server
        return apiClient.createPost(post)
            .handleEvents(receiveOutput: { [weak self] serverPost in
                self?.updatePostSync(serverPost, synced: true)
            })
            .catch { error in
                // Keep local version if sync fails
                Just(savedPost)
            }
            .eraseToAnyPublisher()
    }

    func syncPendingChanges() {
        let unsyncedPosts = fetchUnsyncedPosts()

        unsyncedPosts.forEach { post in
            apiClient.syncPost(post)
                .sink(receiveCompletion: { _ in },
                      receiveValue: { [weak self] in
                    self?.markPostAsSynced(post)
                })
                .store(in: &cancellables)
        }
    }
}
```

### Android Offline-First with Room

```kotlin
class OfflineFirstRepository(
    private val userDao: UserDao,
    private val apiService: ApiService
) {
    fun getUsers(): Flow<List<User>> = flow {
        // 1. Emit cached data first
        val cachedUsers = userDao.getAllUsers().first()
        if (cachedUsers.isNotEmpty()) {
            emit(cachedUsers.map { it.toModel() })
        }

        // 2. Fetch from network and update cache
        try {
            val networkUsers = apiService.fetchUsers()
            userDao.insertAll(networkUsers.map { it.toEntity() })
            emit(networkUsers)
        } catch (e: Exception) {
            // Continue with cached data if network fails
            if (cachedUsers.isEmpty()) {
                throw e
            }
        }
    }.flowOn(Dispatchers.IO)

    suspend fun createUser(user: User): Result<User> {
        return try {
            // 1. Save locally with pending sync flag
            val entity = user.toEntity().copy(syncPending = true)
            userDao.insertUser(entity)

            // 2. Try to sync with server
            val serverUser = apiService.createUser(user)
            userDao.updateUser(serverUser.toEntity().copy(syncPending = false))
            Result.success(serverUser)
        } catch (e: Exception) {
            // Return local version even if sync fails
            Result.success(user)
        }
    }

    suspend fun syncPendingChanges() {
        val pendingUsers = userDao.getPendingUsers()
        pendingUsers.forEach { user ->
            try {
                apiService.syncUser(user.toModel())
                userDao.updateUser(user.copy(syncPending = false))
            } catch (e: Exception) {
                // Will retry later
            }
        }
    }
}
```

## Push Notifications

### iOS Push Notifications (APNS)

```swift
// AppDelegate setup
import UserNotifications

class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        UNUserNotificationCenter.current().delegate = self
        requestNotificationPermission()
        application.registerForRemoteNotifications()

        return true
    }

    func requestNotificationPermission() {
        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
            if granted {
                print("Notification permission granted")
            }
        }
    }

    func application(_ application: UIApplication,
                     didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()
        print("Device Token: \(token)")
        // Send token to your server
    }

    func application(_ application: UIApplication,
                     didReceiveRemoteNotification userInfo: [AnyHashable: Any],
                     fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
        // Handle notification
        handleNotification(userInfo)
        completionHandler(.newData)
    }
}

extension AppDelegate: UNUserNotificationCenterDelegate {
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
                                withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        // Show notification even when app is in foreground
        completionHandler([.banner, .sound, .badge])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
        // Handle notification tap
        let userInfo = response.notification.request.content.userInfo
        handleNotificationTap(userInfo)
        completionHandler()
    }
}

// Local notifications
func scheduleLocalNotification() {
    let content = UNMutableNotificationContent()
    content.title = "Reminder"
    content.body = "Don't forget to check your tasks"
    content.sound = .default

    let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 60, repeats: false)
    let request = UNNotificationRequest(identifier: "reminder", content: content, trigger: trigger)

    UNUserNotificationCenter.current().add(request) { error in
        if let error = error {
            print("Error scheduling notification: \(error)")
        }
    }
}
```

### Android Push Notifications (FCM)

```kotlin
// Firebase Cloud Messaging service
class MyFirebaseMessagingService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        super.onNewToken(token)
        Log.d("FCM", "Token: $token")
        // Send token to your server
        sendTokenToServer(token)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)

        remoteMessage.notification?.let { notification ->
            showNotification(
                title = notification.title ?: "",
                body = notification.body ?: ""
            )
        }

        remoteMessage.data.isNotEmpty().let {
            handleDataPayload(remoteMessage.data)
        }
    }

    private fun showNotification(title: String, body: String) {
        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

        // Create notification channel (required for Android 8.0+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "Default Channel",
                NotificationManager.IMPORTANCE_DEFAULT
            )
            notificationManager.createNotificationChannel(channel)
        }

        val intent = Intent(this, MainActivity::class.java)
        val pendingIntent = PendingIntent.getActivity(
            this, 0, intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle(title)
            .setContentText(body)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true)
            .build()

        notificationManager.notify(NOTIFICATION_ID, notification)
    }

    companion object {
        private const val CHANNEL_ID = "default_channel"
        private const val NOTIFICATION_ID = 1
    }
}

// Request notification permission (Android 13+)
@RequiresApi(Build.VERSION_CODES.TIRAMISU)
fun requestNotificationPermission(activity: Activity) {
    ActivityCompat.requestPermissions(
        activity,
        arrayOf(Manifest.permission.POST_NOTIFICATIONS),
        NOTIFICATION_PERMISSION_REQUEST_CODE
    )
}
```

## Deep Linking

### iOS Universal Links

```swift
// Associated domains in Xcode: applinks:yourdomain.com

// AppDelegate or SceneDelegate
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {

    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else {
        return false
    }

    handleDeepLink(url)
    return true
}

func handleDeepLink(_ url: URL) {
    // Parse URL: https://yourdomain.com/user/123
    let components = URLComponents(url: url, resolvingAgainstBaseURL: true)

    switch components?.path {
    case "/user":
        if let userId = components?.queryItems?.first(where: { $0.name == "id" })?.value {
            navigateToUser(userId: userId)
        }
    case "/post":
        if let postId = components?.queryItems?.first(where: { $0.name == "id" })?.value {
            navigateToPost(postId: postId)
        }
    default:
        break
    }
}
```

### Android Deep Links & App Links

```kotlin
// AndroidManifest.xml
/*
<activity android:name=".MainActivity">
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="https"
            android:host="yourdomain.com"
            android:pathPrefix="/user" />
    </intent-filter>
</activity>
*/

// Handle deep link in Activity
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        handleDeepLink(intent)
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        intent?.let { handleDeepLink(it) }
    }

    private fun handleDeepLink(intent: Intent) {
        val data = intent.data ?: return

        when (data.path) {
            "/user" -> {
                val userId = data.getQueryParameter("id")
                navigateToUser(userId)
            }
            "/post" -> {
                val postId = data.getQueryParameter("id")
                navigateToPost(postId)
            }
        }
    }
}
```

## In-App Purchases

### iOS StoreKit

```swift
import StoreKit

class IAPManager: NSObject, ObservableObject {
    @Published var products: [Product] = []
    private var updateListenerTask: Task<Void, Error>?

    override init() {
        super.init()
        updateListenerTask = listenForTransactions()
    }

    func loadProducts() async {
        do {
            let productIds = ["com.app.premium", "com.app.coins_100"]
            products = try await Product.products(for: productIds)
        } catch {
            print("Failed to load products: \(error)")
        }
    }

    func purchase(_ product: Product) async throws -> Transaction? {
        let result = try await product.purchase()

        switch result {
        case .success(let verification):
            let transaction = try checkVerified(verification)
            await transaction.finish()
            return transaction

        case .userCancelled:
            return nil

        case .pending:
            return nil

        @unknown default:
            return nil
        }
    }

    func listenForTransactions() -> Task<Void, Error> {
        return Task.detached {
            for await result in Transaction.updates {
                do {
                    let transaction = try self.checkVerified(result)
                    await self.handlePurchase(transaction)
                    await transaction.finish()
                } catch {
                    print("Transaction verification failed")
                }
            }
        }
    }

    func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
        switch result {
        case .unverified:
            throw IAPError.unverifiedTransaction
        case .verified(let safe):
            return safe
        }
    }

    func handlePurchase(_ transaction: Transaction) async {
        // Grant access to premium content
        switch transaction.productID {
        case "com.app.premium":
            UserDefaults.standard.set(true, forKey: "isPremium")
        case "com.app.coins_100":
            addCoins(100)
        default:
            break
        }
    }
}
```

### Android Google Play Billing

```kotlin
class BillingManager(private val activity: Activity) {
    private lateinit var billingClient: BillingClient
    private val purchasesUpdatedListener = PurchasesUpdatedListener { billingResult, purchases ->
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK && purchases != null) {
            for (purchase in purchases) {
                handlePurchase(purchase)
            }
        }
    }

    fun initialize() {
        billingClient = BillingClient.newBuilder(activity)
            .setListener(purchasesUpdatedListener)
            .enablePendingPurchases()
            .build()

        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(billingResult: BillingResult) {
                if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                    queryProducts()
                }
            }

            override fun onBillingServiceDisconnected() {
                // Retry connection
            }
        })
    }

    private fun queryProducts() {
        val productList = listOf(
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("premium_monthly")
                .setProductType(BillingClient.ProductType.SUBS)
                .build()
        )

        val params = QueryProductDetailsParams.newBuilder()
            .setProductList(productList)
            .build()

        billingClient.queryProductDetailsAsync(params) { billingResult, productDetailsList ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                // Show products
            }
        }
    }

    fun purchase(productDetails: ProductDetails) {
        val productDetailsParamsList = listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                .setProductDetails(productDetails)
                .build()
        )

        val billingFlowParams = BillingFlowParams.newBuilder()
            .setProductDetailsParamsList(productDetailsParamsList)
            .build()

        billingClient.launchBillingFlow(activity, billingFlowParams)
    }

    private fun handlePurchase(purchase: Purchase) {
        if (purchase.purchaseState == Purchase.PurchaseState.PURCHASED) {
            if (!purchase.isAcknowledged) {
                acknowledgePurchase(purchase)
            }
            // Grant access to content
            grantPremiumAccess()
        }
    }

    private fun acknowledgePurchase(purchase: Purchase) {
        val acknowledgePurchaseParams = AcknowledgePurchaseParams.newBuilder()
            .setPurchaseToken(purchase.purchaseToken)
            .build()

        billingClient.acknowledgePurchase(acknowledgePurchaseParams) { billingResult ->
            if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
                // Purchase acknowledged
            }
        }
    }
}
```

## Mobile Security

### iOS Keychain

```swift
import Security

class KeychainManager {
    enum KeychainError: Error {
        case duplicateItem
        case itemNotFound
        case unexpectedStatus(OSStatus)
    }

    func save(key: String, value: String) throws {
        let data = value.data(using: .utf8)!

        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecValueData as String: data
        ]

        let status = SecItemAdd(query as CFDictionary, nil)

        guard status != errSecDuplicateItem else {
            throw KeychainError.duplicateItem
        }

        guard status == errSecSuccess else {
            throw KeychainError.unexpectedStatus(status)
        }
    }

    func get(key: String) throws -> String {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]

        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)

        guard status != errSecItemNotFound else {
            throw KeychainError.itemNotFound
        }

        guard status == errSecSuccess,
              let data = result as? Data,
              let value = String(data: data, encoding: .utf8) else {
            throw KeychainError.unexpectedStatus(status)
        }

        return value
    }

    func delete(key: String) throws {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key
        ]

        let status = SecItemDelete(query as CFDictionary)

        guard status == errSecSuccess || status == errSecItemNotFound else {
            throw KeychainError.unexpectedStatus(status)
        }
    }
}

// Usage
let keychain = KeychainManager()
try? keychain.save(key: "auth_token", value: "abc123")
let token = try? keychain.get(key: "auth_token")
```

### Android Keystore

```kotlin
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec

class KeystoreManager(private val context: Context) {
    private val keyStore = KeyStore.getInstance("AndroidKeyStore").apply { load(null) }
    private val keyAlias = "MyAppKey"

    init {
        createKeyIfNeeded()
    }

    private fun createKeyIfNeeded() {
        if (!keyStore.containsAlias(keyAlias)) {
            val keyGenerator = KeyGenerator.getInstance(
                KeyProperties.KEY_ALGORITHM_AES,
                "AndroidKeyStore"
            )

            val keyGenParameterSpec = KeyGenParameterSpec.Builder(
                keyAlias,
                KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
            )
                .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                .setUserAuthenticationRequired(false)
                .build()

            keyGenerator.init(keyGenParameterSpec)
            keyGenerator.generateKey()
        }
    }

    fun encrypt(data: String): EncryptedData {
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        val secretKey = keyStore.getKey(keyAlias, null) as SecretKey

        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        val iv = cipher.iv
        val encryptedBytes = cipher.doFinal(data.toByteArray())

        return EncryptedData(
            data = Base64.encodeToString(encryptedBytes, Base64.DEFAULT),
            iv = Base64.encodeToString(iv, Base64.DEFAULT)
        )
    }

    fun decrypt(encryptedData: EncryptedData): String {
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        val secretKey = keyStore.getKey(keyAlias, null) as SecretKey

        val iv = Base64.decode(encryptedData.iv, Base64.DEFAULT)
        val spec = GCMParameterSpec(128, iv)

        cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)

        val encryptedBytes = Base64.decode(encryptedData.data, Base64.DEFAULT)
        val decryptedBytes = cipher.doFinal(encryptedBytes)

        return String(decryptedBytes)
    }
}

data class EncryptedData(val data: String, val iv: String)

// Secure SharedPreferences
class SecureStorage(context: Context) {
    private val sharedPreferences = EncryptedSharedPreferences.create(
        context,
        "secure_prefs",
        MasterKey.Builder(context)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .build(),
        EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
        EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
    )

    fun saveToken(token: String) {
        sharedPreferences.edit().putString("auth_token", token).apply()
    }

    fun getToken(): String? {
        return sharedPreferences.getString("auth_token", null)
    }
}
```

## Best Practices

### Performance Optimization

**iOS Performance**:
- Use lazy loading for views and data
- Implement view recycling (UITableView/UICollectionView)
- Optimize image loading (use AsyncImage in SwiftUI, SDWebImage for UIKit)
- Use Instruments to profile (Time Profiler, Allocations, Leaks)
- Reduce view hierarchy complexity
- Cache computed properties
- Use background threads for heavy operations

**Android Performance**:
- Use LazyColumn/LazyRow instead of ScrollView
- Implement pagination for large datasets
- Optimize image loading (Coil, Glide)
- Use Android Profiler (CPU, Memory, Network)
- Reduce overdraw (Debug GPU Overdraw)
- Use ProGuard/R8 for code shrinking
- Enable strict mode in debug builds

### Testing

**iOS Testing**:
```swift
// Unit tests
import XCTest
@testable import MyApp

class UserViewModelTests: XCTestCase {
    var viewModel: UserViewModel!
    var mockRepository: MockUserRepository!

    override func setUp() {
        super.setUp()
        mockRepository = MockUserRepository()
        viewModel = UserViewModel(repository: mockRepository)
    }

    func testLoadUsers() {
        let expectation = XCTestExpectation(description: "Load users")

        viewModel.loadUsers()

        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            XCTAssertEqual(self.viewModel.users.count, 2)
            expectation.fulfill()
        }

        wait(for: [expectation], timeout: 2.0)
    }
}

// UI tests
class MyAppUITests: XCTestCase {
    func testLoginFlow() {
        let app = XCUIApplication()
        app.launch()

        let emailField = app.textFields["Email"]
        emailField.tap()
        emailField.typeText("test@example.com")

        let passwordField = app.secureTextFields["Password"]
        passwordField.tap()
        passwordField.typeText("password123")

        app.buttons["Login"].tap()

        XCTAssertTrue(app.staticTexts["Welcome"].exists)
    }
}
```

**Android Testing**:
```kotlin
// Unit tests
class UserViewModelTest {
    @get:Rule
    val instantExecutorRule = InstantTaskExecutorRule()

    private lateinit var viewModel: UserViewModel
    private lateinit var repository: FakeUserRepository

    @Before
    fun setup() {
        repository = FakeUserRepository()
        viewModel = UserViewModel(repository)
    }

    @Test
    fun `load users updates state`() = runTest {
        viewModel.loadUsers()

        val users = viewModel.users.first()
        assertThat(users).hasSize(2)
    }
}

// UI tests (Compose)
@RunWith(AndroidJUnit4::class)
class LoginScreenTest {
    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun testLoginFlow() {
        composeTestRule.setContent {
            LoginScreen()
        }

        composeTestRule.onNodeWithText("Email")
            .performTextInput("test@example.com")

        composeTestRule.onNodeWithText("Password")
            .performTextInput("password123")

        composeTestRule.onNodeWithText("Login")
            .performClick()

        composeTestRule.onNodeWithText("Welcome")
            .assertIsDisplayed()
    }
}
```

## Summary

Mobile development requires:
1. **Platform Expertise**: Deep knowledge of iOS (Swift/SwiftUI) and Android (Kotlin/Compose)
2. **Architecture**: MVVM, Clean Architecture for maintainability
3. **Offline-First**: Local databases (Core Data/Room) with sync
4. **Modern Patterns**: Reactive programming (Combine/Coroutines), declarative UI
5. **Essential Features**: Push notifications, deep linking, in-app purchases
6. **Security**: Keychain/Keystore for sensitive data
7. **Performance**: Profiling and optimization
8. **Testing**: Comprehensive unit and UI tests

Build native mobile apps that are fast, secure, and provide excellent user experiences on both iOS and Android platforms.
