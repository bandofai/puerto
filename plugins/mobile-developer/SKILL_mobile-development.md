# Mobile Development Skill

## Overview

This skill provides comprehensive patterns and best practices for iOS (Swift/SwiftUI, UIKit) and Android (Kotlin/Jetpack Compose) native development, as well as cross-platform frameworks (React Native, Flutter).

## Core Principles

1. **Platform-First Design**: Respect platform conventions and guidelines
2. **Offline-First**: Apps should work without network connectivity
3. **Performance**: 60fps animations, fast startup, minimal battery drain
4. **Accessibility**: Support screen readers, dynamic type, high contrast
5. **Security**: Secure storage, certificate pinning, obfuscation
6. **Testability**: Unit tests, UI tests, integration tests

## iOS Development (Swift/SwiftUI)

### SwiftUI Architecture (Recommended)

**Project Structure**:
```
MyApp/
├── App/
│   ├── MyApp.swift                    # App entry point
│   └── AppDelegate.swift              # Lifecycle management
├── Features/
│   ├── Authentication/
│   │   ├── Views/
│   │   │   ├── LoginView.swift
│   │   │   └── SignUpView.swift
│   │   ├── ViewModels/
│   │   │   └── AuthViewModel.swift
│   │   └── Models/
│   │       └── User.swift
│   └── Home/
│       ├── Views/
│       ├── ViewModels/
│       └── Models/
├── Core/
│   ├── Networking/
│   │   ├── APIClient.swift
│   │   ├── Endpoint.swift
│   │   └── NetworkError.swift
│   ├── Storage/
│   │   ├── UserDefaults+Extensions.swift
│   │   └── KeychainManager.swift
│   └── Extensions/
│       ├── View+Extensions.swift
│       └── String+Extensions.swift
├── Services/
│   ├── AuthService.swift
│   ├── NotificationService.swift
│   └── AnalyticsService.swift
└── Resources/
    ├── Assets.xcassets
    ├── Localizable.strings
    └── Info.plist
```

### SwiftUI View Pattern (MVVM)

```swift
// View
import SwiftUI

struct ProductListView: View {
    @StateObject private var viewModel = ProductListViewModel()
    @State private var showingFilterSheet = false

    var body: some View {
        NavigationStack {
            ZStack {
                switch viewModel.state {
                case .loading:
                    ProgressView("Loading products...")
                        .progressViewStyle(.circular)

                case .loaded(let products):
                    productList(products: products)

                case .empty:
                    emptyState

                case .error(let message):
                    errorState(message: message)
                }
            }
            .navigationTitle("Products")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button {
                        showingFilterSheet = true
                    } label: {
                        Image(systemName: "line.3.horizontal.decrease.circle")
                    }
                }
            }
            .sheet(isPresented: $showingFilterSheet) {
                FilterView(filters: $viewModel.filters)
            }
            .refreshable {
                await viewModel.refresh()
            }
            .task {
                await viewModel.loadProducts()
            }
        }
    }

    @ViewBuilder
    private func productList(products: [Product]) -> some View {
        List {
            ForEach(products) { product in
                NavigationLink(destination: ProductDetailView(product: product)) {
                    ProductRow(product: product)
                }
            }
        }
        .listStyle(.plain)
    }

    private var emptyState: some View {
        ContentUnavailableView(
            "No Products",
            systemImage: "tray",
            description: Text("No products match your filters")
        )
    }

    @ViewBuilder
    private func errorState(message: String) -> some View {
        ContentUnavailableView {
            Label("Error", systemImage: "exclamationmark.triangle")
        } description: {
            Text(message)
        } actions: {
            Button("Retry") {
                Task {
                    await viewModel.loadProducts()
                }
            }
            .buttonStyle(.borderedProminent)
        }
    }
}

// ViewModel
@MainActor
class ProductListViewModel: ObservableObject {
    enum State {
        case loading
        case loaded([Product])
        case empty
        case error(String)
    }

    @Published var state: State = .loading
    @Published var filters: ProductFilters = .default

    private let productService: ProductService
    private var cancellables = Set<AnyCancellable>()

    init(productService: ProductService = .shared) {
        self.productService = productService

        // React to filter changes
        $filters
            .debounce(for: 0.3, scheduler: DispatchQueue.main)
            .sink { [weak self] _ in
                Task { await self?.loadProducts() }
            }
            .store(in: &cancellables)
    }

    func loadProducts() async {
        state = .loading

        do {
            let products = try await productService.fetchProducts(filters: filters)

            if products.isEmpty {
                state = .empty
            } else {
                state = .loaded(products)
            }
        } catch {
            state = .error(error.localizedDescription)
        }
    }

    func refresh() async {
        await loadProducts()
    }
}

// Model
struct Product: Identifiable, Codable {
    let id: UUID
    let name: String
    let description: String
    let price: Decimal
    let imageURL: URL?
    let category: String
    let inStock: Bool

    enum CodingKeys: String, CodingKey {
        case id, name, description, price, category
        case imageURL = "image_url"
        case inStock = "in_stock"
    }
}
```

### Networking Layer (Modern Swift Concurrency)

```swift
// APIClient.swift
import Foundation

protocol APIClient {
    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T
}

final class DefaultAPIClient: APIClient {
    private let session: URLSession
    private let decoder: JSONDecoder

    init(session: URLSession = .shared) {
        self.session = session

        self.decoder = JSONDecoder()
        self.decoder.keyDecodingStrategy = .convertFromSnakeCase
        self.decoder.dateDecodingStrategy = .iso8601
    }

    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T {
        let request = try endpoint.makeRequest()

        let (data, response) = try await session.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw NetworkError.invalidResponse
        }

        guard (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.httpError(httpResponse.statusCode)
        }

        do {
            return try decoder.decode(T.self, from: data)
        } catch {
            throw NetworkError.decodingError(error)
        }
    }
}

// Endpoint.swift
enum Endpoint {
    case products(filters: ProductFilters)
    case productDetail(id: UUID)
    case createOrder(OrderRequest)
    case login(email: String, password: String)

    var baseURL: URL {
        URL(string: "https://api.example.com")!
    }

    var path: String {
        switch self {
        case .products:
            return "/v1/products"
        case .productDetail(let id):
            return "/v1/products/\(id)"
        case .createOrder:
            return "/v1/orders"
        case .login:
            return "/v1/auth/login"
        }
    }

    var method: HTTPMethod {
        switch self {
        case .products, .productDetail:
            return .get
        case .createOrder, .login:
            return .post
        }
    }

    func makeRequest() throws -> URLRequest {
        var components = URLComponents(url: baseURL.appendingPathComponent(path), resolvingAgainstBaseURL: true)!

        // Add query parameters
        if case .products(let filters) = self {
            components.queryItems = filters.queryItems
        }

        guard let url = components.url else {
            throw NetworkError.invalidURL
        }

        var request = URLRequest(url: url)
        request.httpMethod = method.rawValue
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        // Add auth token if available
        if let token = KeychainManager.shared.authToken {
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }

        // Add body for POST requests
        switch self {
        case .createOrder(let orderRequest):
            request.httpBody = try? JSONEncoder().encode(orderRequest)
        case .login(let email, let password):
            let body = ["email": email, "password": password]
            request.httpBody = try? JSONSerialization.data(withJSONObject: body)
        default:
            break
        }

        return request
    }
}

enum NetworkError: LocalizedError {
    case invalidURL
    case invalidResponse
    case httpError(Int)
    case decodingError(Error)
    case noConnection

    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "Invalid URL"
        case .invalidResponse:
            return "Invalid server response"
        case .httpError(let code):
            return "HTTP error: \(code)"
        case .decodingError(let error):
            return "Failed to decode response: \(error.localizedDescription)"
        case .noConnection:
            return "No internet connection"
        }
    }
}
```

### Offline-First with Core Data

```swift
// DataManager.swift
import CoreData

@MainActor
final class DataManager {
    static let shared = DataManager()

    private let container: NSPersistentContainer

    var context: NSManagedObjectContext {
        container.viewContext
    }

    init() {
        container = NSPersistentContainer(name: "MyApp")

        container.loadPersistentStores { description, error in
            if let error = error {
                fatalError("Core Data failed to load: \(error.localizedDescription)")
            }
        }

        container.viewContext.automaticallyMergesChangesFromParent = true
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
    }

    func save() {
        guard context.hasChanges else { return }

        do {
            try context.save()
        } catch {
            print("Failed to save context: \(error)")
        }
    }
}

// ProductService with offline support
final class ProductService {
    static let shared = ProductService()

    private let apiClient: APIClient
    private let dataManager: DataManager

    init(apiClient: APIClient = DefaultAPIClient(), dataManager: DataManager = .shared) {
        self.apiClient = apiClient
        self.dataManager = dataManager
    }

    func fetchProducts(filters: ProductFilters) async throws -> [Product] {
        // Try network first
        do {
            let products: [Product] = try await apiClient.request(.products(filters: filters))

            // Save to local database
            await saveProductsLocally(products)

            return products
        } catch {
            // Fall back to local data if network fails
            return try await fetchLocalProducts(filters: filters)
        }
    }

    private func saveProductsLocally(_ products: [Product]) async {
        let context = dataManager.context

        for product in products {
            let entity = ProductEntity(context: context)
            entity.id = product.id
            entity.name = product.name
            entity.price = product.price as NSDecimalNumber
            entity.lastUpdated = Date()
        }

        dataManager.save()
    }

    private func fetchLocalProducts(filters: ProductFilters) async throws -> [Product] {
        let request = ProductEntity.fetchRequest()
        request.sortDescriptors = [NSSortDescriptor(keyPath: \ProductEntity.name, ascending: true)]

        let entities = try dataManager.context.fetch(request)
        return entities.map { $0.toProduct() }
    }
}
```

### Push Notifications

```swift
// NotificationService.swift
import UserNotifications

final class NotificationService: NSObject {
    static let shared = NotificationService()

    func requestAuthorization() async throws -> Bool {
        let center = UNUserNotificationCenter.current()

        return try await center.requestAuthorization(options: [.alert, .badge, .sound])
    }

    func registerForRemoteNotifications() {
        DispatchQueue.main.async {
            UIApplication.shared.registerForRemoteNotifications()
        }
    }

    func handleDeviceToken(_ deviceToken: Data) async {
        let token = deviceToken.map { String(format: "%02.2hhx", $0) }.joined()

        // Send token to backend
        do {
            try await APIClient.shared.updateDeviceToken(token)
        } catch {
            print("Failed to update device token: \(error)")
        }
    }
}

// AppDelegate.swift
class AppDelegate: NSObject, UIApplicationDelegate, UNUserNotificationCenterDelegate {
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        Task {
            await NotificationService.shared.handleDeviceToken(deviceToken)
        }
    }

    func application(
        _ application: UIApplication,
        didFailToRegisterForRemoteNotificationsWithError error: Error
    ) {
        print("Failed to register for notifications: \(error)")
    }

    // Handle notification when app is in foreground
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification
    ) async -> UNNotificationPresentationOptions {
        return [.banner, .sound, .badge]
    }

    // Handle notification tap
    func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        didReceive response: UNNotificationResponse
    ) async {
        let userInfo = response.notification.request.content.userInfo

        // Handle deep link from notification
        if let deepLink = userInfo["deep_link"] as? String {
            await handleDeepLink(deepLink)
        }
    }
}
```

### Deep Linking

```swift
// DeepLinkHandler.swift
enum DeepLink {
    case product(id: UUID)
    case category(name: String)
    case profile
    case order(id: UUID)

    init?(url: URL) {
        let components = URLComponents(url: url, resolvingAgainstBaseURL: true)

        guard let host = components?.host else { return nil }

        switch host {
        case "product":
            guard let id = components?.queryItems?.first(where: { $0.name == "id" })?.value,
                  let uuid = UUID(uuidString: id) else { return nil }
            self = .product(id: uuid)

        case "category":
            guard let name = components?.queryItems?.first(where: { $0.name == "name" })?.value else { return nil }
            self = .category(name: name)

        case "profile":
            self = .profile

        case "order":
            guard let id = components?.queryItems?.first(where: { $0.name == "id" })?.value,
                  let uuid = UUID(uuidString: id) else { return nil }
            self = .order(id: uuid)

        default:
            return nil
        }
    }
}

@MainActor
final class DeepLinkHandler: ObservableObject {
    @Published var activeDeepLink: DeepLink?

    func handle(_ url: URL) {
        guard let deepLink = DeepLink(url: url) else { return }
        activeDeepLink = deepLink
    }
}

// In App
@main
struct MyApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    @StateObject private var deepLinkHandler = DeepLinkHandler()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(deepLinkHandler)
                .onOpenURL { url in
                    deepLinkHandler.handle(url)
                }
        }
    }
}
```

## Android Development (Kotlin/Jetpack Compose)

### Jetpack Compose Architecture (MVVM + Clean Architecture)

**Project Structure**:
```
app/
├── src/main/
│   ├── java/com/example/myapp/
│   │   ├── MyApplication.kt
│   │   ├── di/                           # Dependency Injection (Hilt)
│   │   │   ├── AppModule.kt
│   │   │   ├── NetworkModule.kt
│   │   │   └── DatabaseModule.kt
│   │   ├── data/
│   │   │   ├── remote/
│   │   │   │   ├── api/
│   │   │   │   │   ├── ApiService.kt
│   │   │   │   │   └── dto/
│   │   │   │   └── interceptor/
│   │   │   ├── local/
│   │   │   │   ├── dao/
│   │   │   │   │   └── ProductDao.kt
│   │   │   │   ├── entity/
│   │   │   │   │   └── ProductEntity.kt
│   │   │   │   └── database/
│   │   │   │       └── AppDatabase.kt
│   │   │   └── repository/
│   │   │       └── ProductRepositoryImpl.kt
│   │   ├── domain/
│   │   │   ├── model/
│   │   │   │   └── Product.kt
│   │   │   ├── repository/
│   │   │   │   └── ProductRepository.kt
│   │   │   └── usecase/
│   │   │       ├── GetProductsUseCase.kt
│   │   │       └── GetProductDetailUseCase.kt
│   │   └── presentation/
│   │       ├── navigation/
│   │       │   └── NavGraph.kt
│   │       ├── products/
│   │       │   ├── ProductListScreen.kt
│   │       │   ├── ProductListViewModel.kt
│   │       │   └── ProductListState.kt
│   │       ├── detail/
│   │       │   ├── ProductDetailScreen.kt
│   │       │   └── ProductDetailViewModel.kt
│   │       └── components/
│   │           ├── ProductCard.kt
│   │           └── LoadingIndicator.kt
│   └── res/
│       ├── values/
│       │   ├── strings.xml
│       │   ├── colors.xml
│       │   └── themes.xml
│       └── drawable/
└── build.gradle.kts
```

### Jetpack Compose UI (Material 3)

```kotlin
// ProductListScreen.kt
@Composable
fun ProductListScreen(
    viewModel: ProductListViewModel = hiltViewModel(),
    onProductClick: (String) -> Unit
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    val pullRefreshState = rememberPullRefreshState(
        refreshing = state.isRefreshing,
        onRefresh = { viewModel.refresh() }
    )

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Products") },
                actions = {
                    IconButton(onClick = { viewModel.toggleFilter() }) {
                        Icon(Icons.Default.FilterList, contentDescription = "Filter")
                    }
                }
            )
        }
    ) { paddingValues ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .pullRefresh(pullRefreshState)
        ) {
            when {
                state.isLoading && state.products.isEmpty() -> {
                    LoadingIndicator(modifier = Modifier.align(Alignment.Center))
                }

                state.error != null && state.products.isEmpty() -> {
                    ErrorState(
                        message = state.error!!,
                        onRetry = { viewModel.loadProducts() },
                        modifier = Modifier.align(Alignment.Center)
                    )
                }

                state.products.isEmpty() -> {
                    EmptyState(
                        message = "No products found",
                        modifier = Modifier.align(Alignment.Center)
                    )
                }

                else -> {
                    ProductList(
                        products = state.products,
                        onProductClick = onProductClick
                    )
                }
            }

            PullRefreshIndicator(
                refreshing = state.isRefreshing,
                state = pullRefreshState,
                modifier = Modifier.align(Alignment.TopCenter)
            )
        }
    }

    // Show filter bottom sheet
    if (state.showFilter) {
        FilterBottomSheet(
            filters = state.filters,
            onApply = { filters -> viewModel.applyFilters(filters) },
            onDismiss = { viewModel.toggleFilter() }
        )
    }

    // Side effects
    LaunchedEffect(Unit) {
        viewModel.loadProducts()
    }
}

@Composable
private fun ProductList(
    products: List<Product>,
    onProductClick: (String) -> Unit
) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        items(
            items = products,
            key = { it.id }
        ) { product ->
            ProductCard(
                product = product,
                onClick = { onProductClick(product.id) },
                modifier = Modifier.animateItemPlacement()
            )
        }
    }
}

@Composable
private fun ProductCard(
    product: Product,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        onClick = onClick,
        modifier = modifier.fillMaxWidth()
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            AsyncImage(
                model = product.imageUrl,
                contentDescription = product.name,
                modifier = Modifier
                    .size(80.dp)
                    .clip(RoundedCornerShape(8.dp)),
                contentScale = ContentScale.Crop
            )

            Column(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.spacedBy(4.dp)
            ) {
                Text(
                    text = product.name,
                    style = MaterialTheme.typography.titleMedium,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )

                Text(
                    text = product.description,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )

                Spacer(modifier = Modifier.height(4.dp))

                Row(
                    horizontalArrangement = Arrangement.SpaceBetween,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text(
                        text = product.formattedPrice,
                        style = MaterialTheme.typography.titleMedium,
                        color = MaterialTheme.colorScheme.primary,
                        fontWeight = FontWeight.Bold
                    )

                    if (product.inStock) {
                        Text(
                            text = "In Stock",
                            style = MaterialTheme.typography.labelSmall,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }
            }
        }
    }
}

// ProductListViewModel.kt
@HiltViewModel
class ProductListViewModel @Inject constructor(
    private val getProductsUseCase: GetProductsUseCase
) : ViewModel() {

    private val _state = MutableStateFlow(ProductListState())
    val state = _state.asStateFlow()

    fun loadProducts() {
        viewModelScope.launch {
            _state.update { it.copy(isLoading = true, error = null) }

            getProductsUseCase(state.value.filters)
                .onSuccess { products ->
                    _state.update {
                        it.copy(
                            products = products,
                            isLoading = false,
                            isRefreshing = false
                        )
                    }
                }
                .onFailure { error ->
                    _state.update {
                        it.copy(
                            error = error.message,
                            isLoading = false,
                            isRefreshing = false
                        )
                    }
                }
        }
    }

    fun refresh() {
        _state.update { it.copy(isRefreshing = true) }
        loadProducts()
    }

    fun applyFilters(filters: ProductFilters) {
        _state.update { it.copy(filters = filters, showFilter = false) }
        loadProducts()
    }

    fun toggleFilter() {
        _state.update { it.copy(showFilter = !it.showFilter) }
    }
}

data class ProductListState(
    val products: List<Product> = emptyList(),
    val filters: ProductFilters = ProductFilters(),
    val isLoading: Boolean = false,
    val isRefreshing: Boolean = false,
    val error: String? = null,
    val showFilter: Boolean = false
)
```

### Networking with Retrofit + Coroutines

```kotlin
// ApiService.kt
interface ApiService {
    @GET("v1/products")
    suspend fun getProducts(
        @Query("category") category: String? = null,
        @Query("min_price") minPrice: Double? = null,
        @Query("max_price") maxPrice: Double? = null,
        @Query("page") page: Int = 1,
        @Query("limit") limit: Int = 20
    ): Response<ProductsResponse>

    @GET("v1/products/{id}")
    suspend fun getProductDetail(@Path("id") id: String): Response<ProductDetailResponse>

    @POST("v1/orders")
    suspend fun createOrder(@Body order: CreateOrderRequest): Response<OrderResponse>

    @POST("v1/auth/login")
    suspend fun login(@Body credentials: LoginRequest): Response<AuthResponse>
}

// NetworkModule.kt
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideOkHttpClient(
        authInterceptor: AuthInterceptor
    ): OkHttpClient {
        return OkHttpClient.Builder()
            .addInterceptor(authInterceptor)
            .addInterceptor(HttpLoggingInterceptor().apply {
                level = if (BuildConfig.DEBUG) {
                    HttpLoggingInterceptor.Level.BODY
                } else {
                    HttpLoggingInterceptor.Level.NONE
                }
            })
            .connectTimeout(30, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .writeTimeout(30, TimeUnit.SECONDS)
            .build()
    }

    @Provides
    @Singleton
    fun provideRetrofit(okHttpClient: OkHttpClient): Retrofit {
        return Retrofit.Builder()
            .baseUrl("https://api.example.com/")
            .client(okHttpClient)
            .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
            .build()
    }

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService {
        return retrofit.create(ApiService::class.java)
    }
}

// AuthInterceptor.kt
class AuthInterceptor @Inject constructor(
    private val tokenManager: TokenManager
) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): okhttp3.Response {
        val originalRequest = chain.request()

        val token = tokenManager.getAccessToken()

        val request = if (token != null) {
            originalRequest.newBuilder()
                .header("Authorization", "Bearer $token")
                .build()
        } else {
            originalRequest
        }

        return chain.proceed(request)
    }
}
```

### Offline-First with Room

```kotlin
// AppDatabase.kt
@Database(
    entities = [ProductEntity::class],
    version = 1,
    exportSchema = false
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun productDao(): ProductDao
}

// ProductEntity.kt
@Entity(tableName = "products")
data class ProductEntity(
    @PrimaryKey val id: String,
    val name: String,
    val description: String,
    val price: Double,
    val imageUrl: String?,
    val category: String,
    val inStock: Boolean,
    val lastUpdated: Long = System.currentTimeMillis()
)

// ProductDao.kt
@Dao
interface ProductDao {
    @Query("SELECT * FROM products ORDER BY name ASC")
    fun getAllProducts(): Flow<List<ProductEntity>>

    @Query("SELECT * FROM products WHERE category = :category")
    fun getProductsByCategory(category: String): Flow<List<ProductEntity>>

    @Query("SELECT * FROM products WHERE id = :id")
    suspend fun getProductById(id: String): ProductEntity?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertProducts(products: List<ProductEntity>)

    @Query("DELETE FROM products WHERE lastUpdated < :timestamp")
    suspend fun deleteOldProducts(timestamp: Long)
}

// ProductRepositoryImpl.kt
class ProductRepositoryImpl @Inject constructor(
    private val apiService: ApiService,
    private val productDao: ProductDao,
    private val networkMonitor: NetworkMonitor
) : ProductRepository {

    override suspend fun getProducts(filters: ProductFilters): Result<List<Product>> {
        return try {
            // Try network first if connected
            if (networkMonitor.isConnected()) {
                val response = apiService.getProducts(
                    category = filters.category,
                    minPrice = filters.minPrice,
                    maxPrice = filters.maxPrice
                )

                if (response.isSuccessful && response.body() != null) {
                    val products = response.body()!!.products.map { it.toDomain() }

                    // Cache in local database
                    productDao.insertProducts(products.map { it.toEntity() })

                    Result.success(products)
                } else {
                    // Fallback to local data
                    getLocalProducts(filters)
                }
            } else {
                // No network, use local data
                getLocalProducts(filters)
            }
        } catch (e: Exception) {
            // Error occurred, fallback to local data
            getLocalProducts(filters)
        }
    }

    private suspend fun getLocalProducts(filters: ProductFilters): Result<List<Product>> {
        return try {
            val products = if (filters.category != null) {
                productDao.getProductsByCategory(filters.category).first()
            } else {
                productDao.getAllProducts().first()
            }

            Result.success(products.map { it.toDomain() })
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
```

### Push Notifications (FCM)

```kotlin
// MyFirebaseMessagingService.kt
@AndroidEntryPoint
class MyFirebaseMessagingService : FirebaseMessagingService() {

    @Inject
    lateinit var notificationHelper: NotificationHelper

    override fun onNewToken(token: String) {
        super.onNewToken(token)

        // Send token to backend
        CoroutineScope(Dispatchers.IO).launch {
            try {
                // apiService.updateDeviceToken(token)
            } catch (e: Exception) {
                Log.e("FCM", "Failed to update token", e)
            }
        }
    }

    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)

        message.notification?.let { notification ->
            val title = notification.title ?: "New Notification"
            val body = notification.body ?: ""
            val data = message.data

            notificationHelper.showNotification(
                title = title,
                message = body,
                deepLink = data["deep_link"]
            )
        }
    }
}

// NotificationHelper.kt
@Singleton
class NotificationHelper @Inject constructor(
    @ApplicationContext private val context: Context
) {
    private val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

    init {
        createNotificationChannel()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "General Notifications",
                NotificationManager.IMPORTANCE_DEFAULT
            ).apply {
                description = "General app notifications"
                enableVibration(true)
            }

            notificationManager.createNotificationChannel(channel)
        }
    }

    fun showNotification(title: String, message: String, deepLink: String? = null) {
        val intent = Intent(context, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
            deepLink?.let { putExtra("deep_link", it) }
        }

        val pendingIntent = PendingIntent.getActivity(
            context,
            0,
            intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        val notification = NotificationCompat.Builder(context, CHANNEL_ID)
            .setContentTitle(title)
            .setContentText(message)
            .setSmallIcon(R.drawable.ic_notification)
            .setAutoCancel(true)
            .setContentIntent(pendingIntent)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .build()

        notificationManager.notify(System.currentTimeMillis().toInt(), notification)
    }

    companion object {
        private const val CHANNEL_ID = "general_channel"
    }
}
```

### Deep Linking

```kotlin
// Navigation with deep links
@Composable
fun NavGraph(
    navController: NavHostController = rememberNavController()
) {
    NavHost(
        navController = navController,
        startDestination = "products"
    ) {
        composable(
            route = "products",
            deepLinks = listOf(
                navDeepLink { uriPattern = "myapp://products" }
            )
        ) {
            ProductListScreen(
                onProductClick = { productId ->
                    navController.navigate("product/$productId")
                }
            )
        }

        composable(
            route = "product/{productId}",
            deepLinks = listOf(
                navDeepLink { uriPattern = "myapp://product/{productId}" }
            ),
            arguments = listOf(
                navArgument("productId") { type = NavType.StringType }
            )
        ) { backStackEntry ->
            val productId = backStackEntry.arguments?.getString("productId")!!
            ProductDetailScreen(
                productId = productId,
                onBack = { navController.navigateUp() }
            )
        }

        composable(
            route = "profile",
            deepLinks = listOf(
                navDeepLink { uriPattern = "myapp://profile" }
            )
        ) {
            ProfileScreen()
        }
    }
}

// Handle deep links in Activity
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            MyAppTheme {
                val navController = rememberNavController()

                NavGraph(navController = navController)

                // Handle deep links from intent
                LaunchedEffect(intent) {
                    handleDeepLink(intent, navController)
                }
            }
        }
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        // Handle new deep links when app is already running
    }

    private fun handleDeepLink(intent: Intent?, navController: NavHostController) {
        intent?.data?.let { uri ->
            navController.navigate(uri)
        }

        // Handle notification deep links
        intent?.getStringExtra("deep_link")?.let { deepLink ->
            val uri = Uri.parse(deepLink)
            navController.navigate(uri)
        }
    }
}
```

## Cross-Platform Development

### React Native

**Recommended for**:
- Teams with JavaScript/TypeScript expertise
- Apps that don't require complex native features
- Fast MVP development
- Code sharing with web apps

**Architecture**: Redux/Redux Toolkit or Zustand for state management

### Flutter

**Recommended for**:
- Cross-platform consistency priority
- High-performance animations
- Single codebase for iOS/Android/Web
- Teams comfortable with Dart

**Architecture**: BLoC pattern or Riverpod for state management

## Performance Optimization

### iOS Performance

1. **Launch Time**:
   - Minimize work in `didFinishLaunchingWithOptions`
   - Use lazy initialization
   - Defer non-critical tasks

2. **UI Performance**:
   - Use `LazyVStack`/`LazyHStack` for large lists
   - Avoid expensive computations in view body
   - Use `@Published` wisely (avoid unnecessary updates)
   - Profile with Instruments (Time Profiler, Allocations)

3. **Memory Management**:
   - Use `[weak self]` in closures
   - Avoid retain cycles
   - Release large resources promptly
   - Monitor with Instruments (Leaks, Allocations)

4. **Battery Optimization**:
   - Batch network requests
   - Use background tasks appropriately
   - Minimize location updates
   - Optimize animations

### Android Performance

1. **Launch Time**:
   - Minimize Application onCreate work
   - Use lazy initialization (by lazy)
   - Defer non-critical tasks with coroutines
   - Profile with Android Profiler

2. **UI Performance**:
   - Use `LazyColumn`/`LazyRow` instead of Column/Row
   - Minimize recomposition scope
   - Use `remember` and `derivedStateOf`
   - Use `key` parameter in lists
   - Profile with Layout Inspector

3. **Memory Management**:
   - Avoid memory leaks (use lifecycle-aware components)
   - Use appropriate collection sizes
   - Bitmap optimization (downsampling)
   - Monitor with Memory Profiler

4. **Battery Optimization**:
   - Use WorkManager for background tasks
   - Batch network requests
   - Optimize wake locks
   - Implement Doze mode support

## Testing Strategies

### iOS Testing

```swift
// Unit Test
@testable import MyApp
import XCTest

final class ProductViewModelTests: XCTestCase {
    var sut: ProductListViewModel!
    var mockService: MockProductService!

    override func setUp() {
        super.setUp()
        mockService = MockProductService()
        sut = ProductListViewModel(productService: mockService)
    }

    func testLoadProducts_Success() async {
        // Given
        let expectedProducts = [Product.mock(), Product.mock()]
        mockService.productsResult = .success(expectedProducts)

        // When
        await sut.loadProducts()

        // Then
        if case .loaded(let products) = sut.state {
            XCTAssertEqual(products.count, 2)
        } else {
            XCTFail("Expected loaded state")
        }
    }

    func testLoadProducts_Error() async {
        // Given
        mockService.productsResult = .failure(NetworkError.noConnection)

        // When
        await sut.loadProducts()

        // Then
        if case .error(let message) = sut.state {
            XCTAssertFalse(message.isEmpty)
        } else {
            XCTFail("Expected error state")
        }
    }
}

// UI Test
final class ProductListUITests: XCTestCase {
    var app: XCUIApplication!

    override func setUp() {
        super.setUp()
        app = XCUIApplication()
        app.launchArguments = ["UI-Testing"]
        app.launch()
    }

    func testProductList_DisplaysProducts() {
        // Wait for products to load
        let productCell = app.cells.firstMatch
        XCTAssertTrue(productCell.waitForExistence(timeout: 5))

        // Verify product card elements
        XCTAssertTrue(productCell.staticTexts["Product Name"].exists)
        XCTAssertTrue(productCell.staticTexts["$99.99"].exists)
    }

    func testProductList_TapProduct_NavigatesToDetail() {
        // Tap first product
        app.cells.firstMatch.tap()

        // Verify navigation to detail screen
        XCTAssertTrue(app.navigationBars["Product Detail"].waitForExistence(timeout: 2))
    }
}
```

### Android Testing

```kotlin
// Unit Test
class ProductListViewModelTest {
    @get:Rule
    val instantExecutorRule = InstantTaskExecutorRule()

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private lateinit var viewModel: ProductListViewModel
    private lateinit var getProductsUseCase: GetProductsUseCase

    @Before
    fun setup() {
        getProductsUseCase = mockk()
        viewModel = ProductListViewModel(getProductsUseCase)
    }

    @Test
    fun `loadProducts success updates state with products`() = runTest {
        // Given
        val products = listOf(Product.mock(), Product.mock())
        coEvery { getProductsUseCase(any()) } returns Result.success(products)

        // When
        viewModel.loadProducts()

        // Then
        val state = viewModel.state.value
        assertEquals(2, state.products.size)
        assertFalse(state.isLoading)
        assertNull(state.error)
    }

    @Test
    fun `loadProducts error updates state with error message`() = runTest {
        // Given
        val error = Exception("Network error")
        coEvery { getProductsUseCase(any()) } returns Result.failure(error)

        // When
        viewModel.loadProducts()

        // Then
        val state = viewModel.state.value
        assertTrue(state.products.isEmpty())
        assertFalse(state.isLoading)
        assertEquals("Network error", state.error)
    }
}

// UI Test (Compose)
@HiltAndroidTest
class ProductListScreenTest {
    @get:Rule(order = 0)
    val hiltRule = HiltAndroidRule(this)

    @get:Rule(order = 1)
    val composeTestRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun productList_displaysProducts() {
        // Given - products loaded

        // Then
        composeTestRule.onNodeWithText("Product Name").assertIsDisplayed()
        composeTestRule.onNodeWithText("$99.99").assertIsDisplayed()
    }

    @Test
    fun productCard_click_navigatesToDetail() {
        // When
        composeTestRule.onNodeWithText("Product Name").performClick()

        // Then
        composeTestRule.onNodeWithText("Product Detail").assertIsDisplayed()
    }
}
```

## Best Practices Summary

### iOS Best Practices
- Use SwiftUI for new projects
- Follow MVVM architecture
- Use Combine or async/await for async operations
- Implement offline-first with Core Data
- Follow iOS Human Interface Guidelines
- Support accessibility (VoiceOver, Dynamic Type)
- Use SwiftLint for code consistency

### Android Best Practices
- Use Jetpack Compose for new projects
- Follow Clean Architecture + MVVM
- Use Kotlin Coroutines + Flow
- Implement offline-first with Room
- Follow Material Design guidelines
- Support accessibility (TalkBack)
- Use ktlint for code consistency

### Universal Best Practices
- **Security**: Use HTTPS, certificate pinning, secure storage
- **Error Handling**: Graceful degradation, user-friendly messages
- **Testing**: Unit tests, integration tests, UI tests
- **CI/CD**: Automated builds, tests, deployment
- **Analytics**: Track user behavior, crashes, performance
- **Monitoring**: Error tracking (Sentry, Firebase Crashlytics)
- **A/B Testing**: Feature flags, remote config
- **Localization**: Support multiple languages
- **Accessibility**: Screen readers, high contrast, large text
