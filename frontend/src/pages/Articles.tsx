import { PageHeader } from '../components/PageHeader';
import { useArticlesStore } from '../store';

const Articles = () => {
  const { articles } = useArticlesStore();

  return (
    <section>
      <PageHeader title="Latest research dossiers" subtitle="A mock feed of newsroom-ready briefs." />
      <div className="card-grid">
        {articles.map((article) => (
          <article key={article.id} className="card">
            <span className="badge">{article.category}</span>
            <h3>{article.title}</h3>
            <p>{article.excerpt}</p>
            <footer style={{ marginTop: 'auto', display: 'flex', justify-content: 'space-between' }}>
              <small>{new Date(article.publishedAt).toLocaleDateString()}</small>
              <button
                type="button"
                style={{
                  border: 'none',
                  background: 'rgba(252,211,77,0.15)',
                  color: '#fcd34d',
                  borderRadius: '999px',
                  padding: '0.35rem 1rem',
                  cursor: 'pointer',
                }}
              >
                Open brief
              </button>
            </footer>
          </article>
        ))}
      </div>
    </section>
  );
};

export default Articles;
