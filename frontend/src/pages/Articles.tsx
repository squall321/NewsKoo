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
            <span className="badge">{article.valuePropTag}</span>
            <h3>{article.title}</h3>
            <p>{article.excerpt}</p>
            <p className="trust-hint">Category: {article.category}</p>
            <div className="trust-panel">
              <div>
                <p className="trust-label">Source</p>
                <strong>{article.source.outlet}</strong>
                <p className="trust-hint">{article.source.rewriteReason}</p>
              </div>
              <div style={{ textAlign: 'right' }}>
                <p className="trust-label">Status</p>
                <span className={`status-dot ${article.source.status}`}>{article.source.status}</span>
                <a href={article.source.url} target="_blank" rel="noreferrer" className="cta-link">
                  View original
                </a>
              </div>
            </div>
            <footer className="card-footer">
              <small>{new Date(article.publishedAt).toLocaleDateString()}</small>
              <button type="button" className="ghost-button">
                {article.cta.label}
              </button>
            </footer>
            <p className="trust-hint">{article.cta.explanation}</p>
          </article>
        ))}
      </div>
    </section>
  );
};

export default Articles;
